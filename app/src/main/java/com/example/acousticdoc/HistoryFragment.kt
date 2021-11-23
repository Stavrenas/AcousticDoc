package com.example.acousticdoc

import AcousticDoc.databinding.FragmentHistoryBinding
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.recyclerview.widget.RecyclerView

class HistoryFragment: Fragment() {
    private var _binding: FragmentHistoryBinding? = null
    private val binding get() = _binding!!
    private val sharedViewModel: ViewModel by activityViewModels()






    class TextItemViewHolder(val textView: TextView): RecyclerView.ViewHolder(textView)
}