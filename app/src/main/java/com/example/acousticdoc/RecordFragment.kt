package com.example.acousticdoc

import AcousticDoc.databinding.FragmentRecordBinding
import android.os.Bundle
import AcousticDoc.R
import android.content.ContextWrapper
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import android.text.Editable

import android.text.TextWatcher


import android.widget.EditText
import android.widget.Toast

import android.media.MediaRecorder
import android.net.Uri
import android.os.Build
import android.os.Environment
import androidx.annotation.RequiresApi
import androidx.navigation.fragment.findNavController
import java.io.File


class RecordFragment  : Fragment()  {


    private var _binding: FragmentRecordBinding? = null
    private val binding get() = _binding!!
    private val sharedViewModel: ViewModel by activityViewModels()
    private lateinit var mRecorder : WavAudioRecorder
    private var state = 0


    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentRecordBinding.inflate(inflater, container, false)
        return binding.root

    }

    @RequiresApi(Build.VERSION_CODES.S)
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.recording.isEnabled = false

        val myEditText = binding.input as EditText

        myEditText.addTextChangedListener(object : TextWatcher {
            override fun afterTextChanged(s: Editable) {
                //enabled only if string not empty
                binding.recording.isEnabled = myEditText.text.toString() != ""
            }

            override fun beforeTextChanged(s: CharSequence, start: Int, count: Int, after: Int) {}
            override fun onTextChanged(s: CharSequence, start: Int, before: Int, count: Int) {}
        })


        binding.recording.setOnClickListener {


            val fileName = getFilePath().toString() +  "/" + myEditText.text.toString()  + ".wav"

            if (state == 0){
                //recorder setup
                mRecorder = WavAudioRecorder.getInstanse();
                mRecorder.setOutputFile(fileName);
                mRecorder.prepare();
                mRecorder.start();

                binding.recording.setText(R.string.stop_recording)
                binding.input.visibility =View.GONE
                binding.textView2.text = getText(R.string.now_recording)

               // Toast.makeText(context,"Started Recording", Toast.LENGTH_LONG).show()

                state = 1
            }
            else if (state == 1){
                //stop recording, save file and change fragment
                    binding.recording.isEnabled = false

                mRecorder.stop();
                mRecorder.reset();
                sharedViewModel.setModelUri(Uri.fromFile(File(fileName)))
                findNavController().navigate(R.id.action_RecordFragment_to_SoundFragment)
            }
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

    @RequiresApi(Build.VERSION_CODES.S)
    fun getFilePath(): File? {
        val cw = ContextWrapper(activity)
       return cw.getExternalFilesDir(null)
    }

}