package com.acousticdoc.acousticdoc

import AcousticDoc.R
import AcousticDoc.databinding.FragmentSelectBinding
import android.app.Activity
import android.content.ContextWrapper
import android.content.Intent
import android.net.Uri
import android.net.Uri.fromFile
import android.net.Uri.parse
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.navigation.fragment.findNavController
import com.chaquo.python.Python

/**
 * A simple [Fragment] subclass as the default destination in the navigation.
 */
class SelectFragment : Fragment() {

    private var _binding: FragmentSelectBinding? = null
    private val binding get() = _binding!!
    private val sharedViewModel: ViewModel by activityViewModels()

    companion object {
        private const val REQUEST_SOUND_CAPTURE = 1000
        const val REQUEST_SOUND_OPEN = 1
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentSelectBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.select.setOnClickListener {
            popup()
            val intent = Intent(Intent.ACTION_GET_CONTENT)
            intent.type = "audio/*"
            startActivityForResult(intent, 1)

        }

        binding.add.setOnClickListener {
            findNavController().navigate(R.id.action_SelectFragment_to_RecordFragment)
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == REQUEST_SOUND_OPEN && resultCode == Activity.RESULT_OK) {
            val fullSoundUri: Uri? = data?.data
            if (fullSoundUri != null) {
                sharedViewModel.setModelUri(fullSoundUri)
            }
            findNavController().navigate(R.id.action_SelectFragment_to_SoundFragment)
        } else if (requestCode == REQUEST_SOUND_CAPTURE && resultCode == Activity.RESULT_OK) {
            findNavController().navigate(R.id.action_SelectFragment_to_SoundFragment)
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

    private fun popup() {
        Toast.makeText(
            context,
            "?? ???????????????? ???????????? ???? ???????????????????????? ???????? ???????????? ???????? .wav",
            Toast.LENGTH_LONG
        ).show()
    }

}

