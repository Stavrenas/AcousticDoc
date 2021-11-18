package com.example.acousticdoc

import AcousticDoc.R
import AcousticDoc.databinding.FragmentSoundBinding
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
import android.media.MediaPlayer.OnCompletionListener
import android.util.Log


/**
 * A simple [Fragment] subclass as the second destination in the navigation.
 */
class SoundFragment : Fragment() {

    private var _binding: FragmentSoundBinding? = null

    // This property is only valid between onCreateView and
    // onDestroyView.
    private val binding get() = _binding!!
    private val sharedViewModel: ViewModel by activityViewModels()
    var playing = 1
    var mediaPlayer = MediaPlayer()


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
            setOnCompletionListener(
                {
                    if(playing == 0)
                    pauseMusic()
                }
            )
            if (myUri != null) {
                context?.let { setDataSource(it, myUri) }
            }
            prepare()
        }


        binding.play.setOnClickListener {
            toggle()
            //findNavController().navigate(R.id.action_SoundFragment_to_SelectFragment)
        }

        binding.diagnosis.setOnClickListener {
            pauseMusic()

            val selectedId: Int = binding.radioGroup.checkedRadioButtonId
            val selected: String
            if (selectedId == binding.cough.id)
                 selected = "Cough"
            else
                selected = "Breathing"
            Toast.makeText(
                context,
                "$selected ",
                Toast.LENGTH_SHORT
            ).show()
            ////findNavController().navigate(R.id.action_SoundFragment_to_SelectFragment)
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
        binding.play.setText(R.string.play)
    }
     private fun startMusic() {
         val fullSoundUri = sharedViewModel.getModelUri()
         mediaPlayer.start()
         playing = 0
         binding.play.setText(R.string.pause)
         Log.d("URI","URI $fullSoundUri")
     }

    private fun Uri.getName(context: Context): String? {
        val returnCursor = context.contentResolver.query(this, null, null, null, null)
        val nameIndex = returnCursor?.getColumnIndex(OpenableColumns.DISPLAY_NAME)
        returnCursor?.moveToFirst()
        val fileName = nameIndex?.let { returnCursor?.getString(it) }
        returnCursor?.close()
        if(fileName == null) {
          val fullFileName = this.toString()
            return fullFileName.substring(fullFileName.lastIndexOf("/") + 1, fullFileName.length);
        }
        else {
            return fileName
        }
    }



    override fun onDestroyView() {
        if(playing == 0)
        mediaPlayer.pause()
        super.onDestroyView()
        _binding = null

    }
}