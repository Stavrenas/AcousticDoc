
package com.example.acousticdoc.SoundHistory

import AcousticDoc.databinding.FragmentHistoryBinding
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.findNavController
import com.example.acousticdoc.ViewModel
import com.example.acousticdoc.database.SoundHistoryDatabase
import com.example.acousticdoc.database.SoundHistoryViewModelFactory
import com.google.android.material.snackbar.Snackbar

class SoundHistoryFragment : Fragment() {

    private var _binding: FragmentHistoryBinding? = null
    private val binding get() = _binding!!
    private val soundHistoryViewModel: SoundHistoryViewModel by activityViewModels()

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {

        // Get a reference to the binding object and inflate the fragment views.
        _binding = FragmentHistoryBinding.inflate(inflater, container, false)

        val application = requireNotNull(this.activity).application

        // Create an instance of the ViewModel Factory.
        val dataSource = SoundHistoryDatabase.getInstance(application).SoundHistoryDatabaseDao
        val viewModelFactory = SoundHistoryViewModelFactory(dataSource, application)

        // Get a reference to the ViewModel associated with this fragment.
        val soundHistoryViewModel =
            ViewModelProvider(
                this, viewModelFactory).get(SoundHistoryViewModel::class.java)


        val adapter = SoundHistoryAdapter()
        binding.historyList.adapter = adapter

        soundHistoryViewModel.all_history.observe(viewLifecycleOwner, Observer {
            it?.let {
                adapter.data = it
            }
        })


        return binding.root
    }
}