package com.example.acousticdoc

import AcousticDoc.R
import AcousticDoc.databinding.FragmentSoundBinding
import AcousticDoc.ml.Model
import android.content.Context
import android.media.AudioAttributes
import android.media.MediaPlayer
import android.net.Uri
import android.os.Bundle
import android.provider.OpenableColumns
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import android.util.Log
import com.example.acousticdoc.SoundHistory.SoundHistoryFragment
import androidx.fragment.app.FragmentManager
import androidx.navigation.fragment.findNavController
import com.example.acousticdoc.database.SoundHistory
import org.tensorflow.lite.DataType
import org.tensorflow.lite.support.label.TensorLabel
import org.tensorflow.lite.support.tensorbuffer.TensorBuffer
import java.nio.ByteBuffer
import java.nio.ByteBuffer.allocate
import org.tensorflow.lite.support.common.TensorProcessor;
import org.tensorflow.lite.support.common.ops.NormalizeOp;
import kotlin.random.Random


/**
 * A simple [Fragment] subclass as the second destination in the navigation.
 */
class SoundFragment : Fragment() {

    private var _binding: FragmentSoundBinding? = null
    private val binding get() = _binding!!
    private val sharedViewModel: ViewModel by activityViewModels()
    private var playing = 1
    private var mediaPlayer = MediaPlayer()


    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentSoundBinding.inflate(inflater, container, false)
        return binding.root

    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val fullSoundUri = sharedViewModel.getModelUri()

        if (fullSoundUri != null) {
            binding.soundTitle.setText(context?.let { fullSoundUri.getName(it) })
        }
        val myUri: Uri? = sharedViewModel.getModelUri()



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
            pauseMusic()

            val selectedId: Int = binding.radioGroup.checkedRadioButtonId
            var selected: String

            if (selectedId == binding.cough.id) {
                selected = "Cough"
                 val history = SoundHistory(firstName = "Stavr", lastName = "Pip", diagnosis = "COV")

            }
            else {
                selected = "Breathing"
            }

            val model = context?.let { Model.newInstance(it) }

            // Creates inputs for reference.
            val inputFeature0 = TensorBuffer.createFixedSize(intArrayOf(1, 27), DataType.FLOAT32)
            val byteBuffer = inputFeature0.buffer


            for (i in 1..27){
                val rand: Float = Random.nextFloat()
                byteBuffer.putFloat(rand)
            }
            inputFeature0.loadBuffer(byteBuffer)



            val outputs =model?.process(inputFeature0)
            // getting the output
            val outputBuffer = outputs?.outputFeature0AsTensorBuffer

            // adding labels to the output
            val tensorLabel =
                outputBuffer?.let { it1 -> TensorLabel(arrayListOf("Healthy", "Not Healthy"), it1) }

            // getting the first label (hot dog) probability
            // if 80 (you can change that) then we are pretty sure it is a hotdog -> update UI
            val probability = tensorLabel?.mapWithFloatValue?.get("Healthy")
            if (probability != null) {
                sharedViewModel.setProbabilty(probability)
            }


            findNavController().navigate(R.id.action_SoundFragment_to_ResultFragment)

            // Releases model resources if no longer used.
            model?.close()



        }
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
        mediaPlayer.pause()
        playing = 1
        binding.play.setText(AcousticDoc.R.string.play)
    }
     private fun startMusic() {
         val fullSoundUri = sharedViewModel.getModelUri()
         mediaPlayer.start()
         playing = 0
         binding.play.setText(AcousticDoc.R.string.pause)
         Log.d("URI","URI $fullSoundUri")
     }

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
}