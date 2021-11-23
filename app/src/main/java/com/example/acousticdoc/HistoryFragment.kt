package com.example.acousticdoc

import AcousticDoc.databinding.FragmentHistoryBinding
import android.os.Bundle
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.recyclerview.widget.RecyclerView
import com.example.acousticdoc.SoundHistory.SoundHistoryAdapter

class HistoryFragment: Fragment() {
    private var _binding: FragmentHistoryBinding? = null
    private val binding get() = _binding!!
    private val sharedViewModel: ViewModel by activityViewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val adapter = SoundHistoryAdapter()
        binding.historyList.adapter = adapter

    }





    class TextItemViewHolder(val textView: TextView): RecyclerView.ViewHolder(textView)
}