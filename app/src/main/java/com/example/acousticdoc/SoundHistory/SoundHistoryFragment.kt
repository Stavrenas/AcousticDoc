
package com.example.acousticdoc.SoundHistory

import AcousticDoc.databinding.FragmentHistoryBinding
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.example.acousticdoc.database.SoundHistory
import com.example.acousticdoc.database.SoundHistoryDatabase

class SoundHistoryFragment : Fragment() {

    private var _binding: FragmentHistoryBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {

        // Get a reference to the binding object and inflate the fragment views.
        _binding = FragmentHistoryBinding.inflate(inflater, container, false)

        val application = requireNotNull(this.activity).application

        // Create an instance of the ViewModel Factory.
        val dataSource = SoundHistoryDatabase.getInstance(application).soundHistoryDatabaseDao
        val viewModelFactory = SoundHistoryViewModelFactory(dataSource, application)

        // Get a reference to the ViewModel associated with this fragment.
        val soundHistoryViewModel =
            ViewModelProvider(
                this, viewModelFactory).get(SoundHistoryViewModel::class.java)


        val adapter = SoundHistoryAdapter()
        binding.historyList.adapter = adapter

        soundHistoryViewModel.all_history?.observe(viewLifecycleOwner, Observer {
            it?.let {
                adapter.data = it
            }
        })


        return binding.root
    }

    fun add(hist: SoundHistory){
        val application = requireNotNull(this.activity).application

        // Create an instance of the ViewModel Factory.
        val dataSource = SoundHistoryDatabase.getInstance(application).soundHistoryDatabaseDao
        val viewModelFactory = SoundHistoryViewModelFactory(dataSource, application)

        // Get a reference to the ViewModel associated with this fragment.
        val soundHistoryViewModel =
            ViewModelProvider(
                this, viewModelFactory).get(SoundHistoryViewModel::class.java)
        soundHistoryViewModel.insert(hist)
    }
}