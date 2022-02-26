package com.example.acousticdoc

import AcousticDoc.R
import AcousticDoc.databinding.FragmentSoundBinding
import AcousticDoc.ml.CoughCheck
import AcousticDoc.ml.Model
import android.app.AlertDialog
import android.content.Context
import android.content.ContextWrapper
import android.media.AudioAttributes
import android.media.MediaPlayer
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.provider.OpenableColumns
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.annotation.RequiresApi
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.lifecycle.lifecycleScope
import androidx.navigation.fragment.findNavController
import com.chaquo.python.PyException
import com.chaquo.python.Python
import kotlinx.coroutines.*
import org.tensorflow.lite.DataType
import org.tensorflow.lite.support.label.TensorLabel
import org.tensorflow.lite.support.tensorbuffer.TensorBuffer
import java.io.File
import java.lang.Runnable
import java.net.URLDecoder.decode
import java.util.concurrent.Callable


/**
 * A simple [Fragment] subclass as the second destination in the navigation.
 */
class SoundFragment : Fragment() {

    private var _binding: FragmentSoundBinding? = null
    private val binding get() = _binding!!
    private val sharedViewModel: ViewModel by activityViewModels()
    private var playing = 1  //represent playing state of media player
    private var mediaPlayer = MediaPlayer()

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentSoundBinding.inflate(inflater, container, false)
        return binding.root
    }

    @RequiresApi(Build.VERSION_CODES.S)
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val myUri: Uri? = sharedViewModel.getModelUri()

        //set sound file title text from uri
        if (myUri != null)
            binding.soundTitle.text = context?.let { decode(myUri.getName(it)) }

        //initialize player
        mediaPlayer = MediaPlayer().apply {
            setAudioAttributes(
                AudioAttributes.Builder()
                    .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                    .setUsage(AudioAttributes.USAGE_MEDIA)
                    .build()
            )
            setOnCompletionListener {
                if (playing == 0)
                    pauseMusic()
            }
            if (myUri != null) {
                context?.let { setDataSource(it, myUri) }
            }
            prepare()
        }


        binding.play.setOnClickListener {
            toggle()
        }

        binding.Diagnosis.setOnClickListener {
            //create two jobs to update the ui and run audio file processing simultaneously

            //audio processing
            val job = viewLifecycleOwner.lifecycleScope.launch  {
                val probability = withContext(Dispatchers.Default){
                    diagnosis()
                }
                sharedViewModel.setProbability(probability)
            }

            //UI updating
            MainScope().launch {
                //show progress bar when the diagnosis button is pressed
                binding.Diagnosis.visibility = View.GONE
                binding.processing.text = "Επεξεργασία αρχείου..."
                binding.progress.isIndeterminate = true
                binding.processing.visibility = View.VISIBLE
                binding.progress.visibility = View.VISIBLE

                //wait for the audio processing to complete
                job.join()

                withContext(Dispatchers.Main) {

                    val probability = sharedViewModel.getProbability()

                    if (probability != null) {
                        if (probability >= 0) {
                            sharedViewModel.setProbability(probability)
                            findNavController().navigate(R.id.action_SoundFragment_to_ResultFragment)
                        } else {
                            binding.Diagnosis.visibility = View.VISIBLE
                            binding.processing.visibility = View.GONE
                            binding.progress.visibility = View.GONE

                            AlertDialog.Builder(context)
                                .setTitle("Δεν εντοπίστηκε Βήχας")
                                .setMessage("Δεν υπάρχει ήχος βήχα σε αυτό το αρχείο. Δοκιμάστε ξανά.")
                                .setPositiveButton("Εντάξει", null)
                                .show()
                            findNavController().navigate(R.id.action_SoundFragment_to_SelectFragment)
                        }
                    }
                }
            }
        }
    }

    @RequiresApi(Build.VERSION_CODES.S)
    fun diagnosis(): Float{
        val py = Python.getInstance()
        val module = py.getModule("main")

        // Creates inputs for the covid detection model and the model itself
        val numFeatures = 270
        val inputFeature0 =
            TensorBuffer.createFixedSize(intArrayOf(1, numFeatures), DataType.FLOAT32)
        val byteBuffer = inputFeature0.buffer
        val model = context?.let { Model.newInstance(it) }
        var probability = 0f


        //create Filename to pass to the python function to create mulitple audio files containing a cough each
        var filename = ""
        val uri = sharedViewModel.getModelUri()
        if (uri != null) {
            val array =
                context?.let { it1 -> uri.getName(it1) }.toString().split(".wav")
            filename = array[0]
        }


        //find total files containing a cough each
        var files = 0
        try {
            val stream = uri?.let { it1 -> context?.contentResolver?.openInputStream(it1) }
            val content = stream?.readBytes()
            files = module.callAttr("cough_save", content, filename).toInt()
        } catch (e: PyException) {
            Toast.makeText(context, e.message, Toast.LENGTH_LONG).show()
        }


        //Check each produced file and test if it is considered as a cough
        //if yes, proceed to feature extraction
        var coughFiles = 0
        for (fileNumber in 0..files) {

            //Get produced filename
            val slicedFileName =
                getFilePath().toString() + "/" + filename + "_" + fileNumber.toString() + ".wav"
            val slicedUri = Uri.fromFile(File(slicedFileName))
            val slicedStream = slicedUri?.let { it1 -> context?.contentResolver?.openInputStream(it1) }
            val slicedContent = slicedStream?.readBytes()


            //create cough detection model and input buffer
            val coughCheckNumFeatures = 40
            val inputFeature1 =
                TensorBuffer.createFixedSize(intArrayOf(1, coughCheckNumFeatures), DataType.FLOAT32)
            val byteBuffer1 = inputFeature1.buffer
            val model1 = context?.let { it1 -> CoughCheck.newInstance(it1) }

            //extract audio features
            try {
                val coughCheckFeatures =module.callAttr("features_extractor_cough_check", slicedContent).toJava(FloatArray::class.java)
                for (i in 0 until coughCheckNumFeatures) {byteBuffer1.putFloat(i,coughCheckFeatures[i])}
                inputFeature1.loadBuffer(byteBuffer1)
            } catch (e: PyException) {
                Toast.makeText(context, e.message, Toast.LENGTH_LONG).show()
            }

            //run inference
            val coughOutputs = model1?.process(inputFeature1)
            val coughOutputBuffer = coughOutputs?.outputFeature0AsTensorBuffer

            // adding labels to the output
            val coughTensorLabel =
                coughOutputBuffer?.let { it1 ->
                    TensorLabel(
                        arrayListOf(
                            "Cough",
                            "Not Cough"
                        ), it1
                    )
                }


            val coughProbability = coughTensorLabel?.mapWithFloatValue?.get("Cough")!!
            //if the file contains a cough, extract features for covid detection
            if (coughProbability > 0.7) {
                coughFiles += 1
                try {
                    val features = module.callAttr("extract", slicedContent).toJava(FloatArray::class.java)
                    for (i in 0 until numFeatures) {  byteBuffer.putFloat(i, features[i]) }
                    inputFeature0.loadBuffer(byteBuffer)
                    for (i in 0 until numFeatures) {
                        val s = byteBuffer[i].toFloat()
                        Log.d("Out", "$s")
                    }
                } catch (e: PyException) {
                    e.message?.let { Log.d("Python", it) }
                }


                val outputs = model?.process(inputFeature0)
                val outputBuffer = outputs?.outputFeature0AsTensorBuffer

                // adding labels to the output
                val tensorLabel =
                    outputBuffer?.let { it1 ->
                        TensorLabel(
                            arrayListOf(
                                "Healthy",
                                "Not Healthy"
                            ), it1
                        )
                    }

                // getting the first label (Healthy) probability
                probability += tensorLabel?.mapWithFloatValue?.get("Healthy")!!
            }

        }

        if(coughFiles > 0)
            probability /= (coughFiles+1)
        else
            probability = -1f

        return probability
    }

    private fun toggle(){
            if (playing == 1){
                startMusic()
            }
            else {
                pauseMusic()
            }
        }

    private fun pauseMusic(){
        if (playing!=1){
            mediaPlayer.pause()
            playing = 1
            binding.play.setText(R.string.play)
        }
    }

     private fun startMusic() {
         val fullSoundUri = sharedViewModel.getModelUri()
         mediaPlayer.start()
         playing = 0
         binding.play.setText(R.string.pause)
         Log.d("URI","URI $fullSoundUri")
     }

    //Hack to get funky file name from URI
    private fun Uri.getName(context: Context): String {
        val returnCursor = context.contentResolver.query(this, null, null, null, null)
        val nameIndex = returnCursor?.getColumnIndex(OpenableColumns.DISPLAY_NAME)
        returnCursor?.moveToFirst()
        val fileName = nameIndex?.let { returnCursor.getString(it) }
        returnCursor?.close()
        return if(fileName == null) {
            val fullFileName = this.toString()
            fullFileName.substring(fullFileName.lastIndexOf("/") + 1, fullFileName.length)
        } else {
            fileName
        }
    }

    override fun onDestroyView() {
        if(playing == 0)
        mediaPlayer.pause()
        super.onDestroyView()
        _binding = null
    }

    @RequiresApi(Build.VERSION_CODES.S)
    fun getFilePath(): File? {
        val cw = ContextWrapper(activity)
        return cw.getExternalFilesDir(null)
    }

}



