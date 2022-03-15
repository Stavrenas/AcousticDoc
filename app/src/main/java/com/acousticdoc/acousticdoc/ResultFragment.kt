package com.acousticdoc.acousticdoc

import AcousticDoc.R
import AcousticDoc.databinding.FragmentResultBinding
import android.graphics.Color
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
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
        var probability = sharedViewModel.getProbability()

        var positiveProbability = 0f
        var negativeProbability = 0f
        var finalProbability = 0f

        if (probability != null) {
            positiveProbability= probability[0].toFloat()
            negativeProbability= probability[1].toFloat()
        }
        if (probability != null) {
            if (positiveProbability > negativeProbability){
                finalProbability = positiveProbability
                binding.health.setText(R.string.healthy)
                binding.health.setTextColor(Color.GREEN)
                binding.probText.setText(R.string.positive_probability)
                binding.prob.setTextColor(Color.GREEN)
            }
            else {
                finalProbability = negativeProbability
                binding.health.setText(R.string.unhealthy)
                binding.health.setTextColor(Color.RED)
                binding.probText.setText(R.string.negative_probability)
                binding.prob.setTextColor(Color.RED)
            }
        }
        //Enable this to display probability on result screen
        finalProbability = finalProbability.times(100)
        var text = "%.0f".format(finalProbability)
        text += "%"
        binding.prob.text = text
        binding.probText.visibility=View.VISIBLE
    }

}