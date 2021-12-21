package com.example.acousticdoc.SoundHistory

import android.app.Application
import androidx.lifecycle.*
import com.example.acousticdoc.database.SoundHistoryDatabaseDao
import com.example.acousticdoc.database.SoundHistory
import kotlinx.coroutines.launch

class SoundHistoryViewModel (dataSource: SoundHistoryDatabaseDao,
                             application: Application
) : ViewModel() {

    /**
     * Hold a reference to SleepDatabase via SleepDatabaseDao.
     */
    val database = dataSource

    private var last = MutableLiveData<SoundHistory?>()

    val all_history = database.getAllHistory()



    init {
        initializeLast()
    }

    private fun initializeLast() {
        viewModelScope.launch {
            //last.value = getLastFromDatabase()
        }
    }

    private fun getLastFromDatabase(): SoundHistory? {
        return database.getLast()
    }

    fun insert(history: SoundHistory) {
        database.insert(history)
    }

    private fun update(history: SoundHistory) {
        database.update(history)
    }


//    /**
//     * Executes when the START button is clicked.
//     */
//    fun onStart() {
//        viewModelScope.launch {
//            // Create a new night, which captures the current time,
//            // and insert it into the database.
//            val newHistory = SoundHistory()
//
//            insert(newHistory)
//
//            last.value = getLastFromDatabase()
//        }
//    }

//    /**
//     * Executes when the STOP button is clicked.
//     */
//    fun onStop() {
//        viewModelScope.launch {
//            // In Kotlin, the return@label syntax is used for specifying which function among
//            // several nested ones this statement returns from.
//            // In this case, we are specifying to return from launch().
//            val oldNight = last.value ?: return@launch
//
//            // Update the night in the database to add the end time.
//            oldNight.endTimeMilli = System.currentTimeMillis()
//
//            update(oldNight)
//
//            // Set state to navigate to the SleepQualityFragment.
//            _navigateToSleepQuality.value = oldNight
//        }
//    }
//
//    /**
//     * Executes when the CLEAR button is clicked.
//     */
//    fun onClear() {
//        viewModelScope.launch {
//            // Clear the database table.
//            clear()
//
//            // And clear tonight since it's no longer in the database
//            last.value = null
//
//            // Show a snackbar message, because it's friendly.
//            _showSnackbarEvent.value = true
//        }
//    }
}