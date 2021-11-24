
package com.example.android.trackmysleepquality.sleeptracker

import AcousticDoc.databinding.FragmentHistoryBinding
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.findNavController
import com.example.acousticdoc.SoundHistory.SoundHistoryAdapter
import com.example.acousticdoc.SoundHistory.SoundHistoryViewModel
import com.example.acousticdoc.database.SoundHistoryDatabase
import com.example.acousticdoc.database.SoundHistoryViewModelFactory
import com.google.android.material.snackbar.Snackbar

class SoundHistoryFragment : Fragment() {

    private var _binding: FragmentHistoryBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {

        // Get a reference to the binding object and inflate the fragment views.
        _binding = FragmentHistoryBinding.inflate(inflater, container, false)

        val application = requireNotNull(this.activity).application

        // Create an instance of the ViewModel Factory.
        val dataSource = SoundHistoryDatabase.getInstance(application).SoundHistoryDatabaseDao
        val viewModelFactory = SoundHistoryViewModelFactory(dataSource, application)

        // Get a reference to the ViewModel associated with this fragment.
        val sleepTrackerViewModel =
            ViewModelProvider(
                this, viewModelFactory).get(SoundHistoryViewModel::class.java)

        // To use the View Model with data binding, you have to explicitly
        // give the binding object a reference to it.
        binding.soundHistoryViewModel = sleepTrackerViewModel

        val adapter = SoundHistoryAdapter()
        binding.historyList.adapter = adapter

        sleepTrackerViewModel.all_history.observe(viewLifecycleOwner, Observer {
            it?.let {
                adapter.data = it
            }
        })

        // Specify the current activity as the lifecycle owner of the binding.
        // This is necessary so that the binding can observe LiveData updates.
        binding.setLifecycleOwner(this)

        // Add an Observer on the state variable for showing a Snackbar message
        // when the CLEAR button is pressed.
        sleepTrackerViewModel.showSnackBarEvent.observe(viewLifecycleOwner, Observer {
            if (it == true) { // Observed state is true.
                Snackbar.make(
                    requireActivity().findViewById(android.R.id.content),
                    getString(R.string.cleared_message),
                    Snackbar.LENGTH_SHORT // How long to display the message.
                ).show()
                // Reset state to make sure the toast is only shown once, even if the device
                // has a configuration change.
                sleepTrackerViewModel.doneShowingSnackbar()
            }
        })

        // Add an Observer on the state variable for Navigating when STOP button is pressed.
        sleepTrackerViewModel.navigateToSoundHistory.observe(viewLifecycleOwner, Observer { night ->
            night?.let {
                // We need to get the navController from this, because button is not ready, and it
                // just has to be a view. For some reason, this only matters if we hit stop again
                // after using the back button, not if we hit stop and choose a quality.
                // Also, in the Navigation Editor, for Quality -> Tracker, check "Inclusive" for
                // popping the stack to get the correct behavior if we press stop multiple times
                // followed by back.
                // Also: https://stackoverflow.com/questions/28929637/difference-and-uses-of-oncreate-oncreateview-and-onactivitycreated-in-fra
                this.findNavController().navigate(
                    SleepTrackerFragmentDirections
                        .actionSleepTrackerFragmentToSleepQualityFragment(night.nightId))
                // Reset state to make sure we only navigate once, even if the device
                // has a configuration change.
                sleepTrackerViewModel.doneNavigating()
            }
        })
        return binding.root
    }
}