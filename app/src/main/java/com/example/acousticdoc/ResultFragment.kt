package com.example.acousticdoc

import AcousticDoc.R
import AcousticDoc.databinding.FragmentResultBinding
import AcousticDoc.databinding.FragmentSoundBinding
import android.graphics.Color
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels

class ResultFragment: Fragment() {
    private var _binding: FragmentResultBinding? = null
    private val binding get() = _binding!!
    private val sharedViewModel: ViewModel by activityViewModels()




    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentResultBinding.inflate(inflater, container, false)
        return binding.root

    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        var probability = sharedViewModel.getProbabitly()

        if (probability != null) {
            probability= probability.toFloat()
        }
        if (probability != null) {
            if (probability > 0.5F){
                binding.health.setText(R.string.healthy)
                binding.health.setTextColor(Color.GREEN)
            }
            else if (probability < 0.5F){
                binding.health.setText(R.string.unhealthy)
                binding.health.setTextColor(Color.RED)
            }
        }
        //binding.prob.text = probability!!.toString()

    }


}