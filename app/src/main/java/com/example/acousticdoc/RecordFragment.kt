package com.example.acousticdoc

import AcousticDoc.databinding.FragmentRecordBinding
import android.os.Bundle
import AcousticDoc.R
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import android.text.Editable

import android.text.TextWatcher


import android.widget.EditText
import android.widget.Toast


class RecordFragment  : Fragment()  {


    private var _binding: FragmentRecordBinding? = null

    // This property is only valid between onCreateView and
    // onDestroyView.
    private val binding get() = _binding!!
    private val sharedViewModel: ViewModel by activityViewModels()
    var state =0

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentRecordBinding.inflate(inflater, container, false)
        return binding.root

    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.recording.isEnabled = false

        var myEditText = binding.input as EditText

        myEditText.addTextChangedListener(object : TextWatcher {
            override fun afterTextChanged(s: Editable) {
                if (myEditText.text.toString() == ""){
                    binding.recording.isEnabled = false
                }
                else{
                    binding.recording.isEnabled = true
                }

                // you can call or do what you want with your EditText here

                // yourEditText...
            }

            override fun beforeTextChanged(s: CharSequence, start: Int, count: Int, after: Int) {}
            override fun onTextChanged(s: CharSequence, start: Int, before: Int, count: Int) {
//                if (myEditText.text.toString() == ""){
//                    binding.recording.isEnabled = false
//                }
//                else{
//                    binding.recording.isEnabled = true
//                }
            }
        })


        binding.recording.setOnClickListener {
            if (state == 0){
                binding.recording.setText(R.string.stop_recording)
                binding.input.visibility =View.GONE
                binding.textView2.visibility = View.GONE
                binding.textView5.visibility = View.VISIBLE
                Toast.makeText(context,"Started Recording", Toast.LENGTH_LONG)

                state = 1
            }
            else if (state == 1){
                binding.recording.isEnabled = false
                Toast.makeText(context,"Stopped Recording", Toast.LENGTH_LONG)
            }




        }




    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null

    }

}