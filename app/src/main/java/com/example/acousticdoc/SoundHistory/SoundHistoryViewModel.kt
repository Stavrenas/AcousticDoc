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

    /**
     * Converted nights to Spanned for displaying.
     */
    val historyString = Transformations.map(all_history) { all_history ->
        formatAllHistory(all_history, application.resources)
    }


    /**
     * Request a toast by setting this value to true.
     *
     * This is private because we don't want to expose setting this value to the Fragment.
     */
    private var _showSnackbarEvent = MutableLiveData<Boolean?>()

    /**
     * If this is true, immediately `show()` a toast and call `doneShowingSnackbar()`.
     */
    val showSnackBarEvent: LiveData<Boolean?>
    get() = _showSnackbarEvent

    /**
     * Variable that tells the Fragment to navigate to a specific [SleepQualityFragment]
     *
     * This is private because we don't want to expose setting this value to the Fragment.
     */
    private val _navigateToSoundHistory = MutableLiveData<SoundHistory>()

    /**
     * If this is non-null, immediately navigate to [SleepQualityFragment] and call [doneNavigating]
     */
    val navigateToSoundHistory: LiveData<SoundHistory>
    get() = _navigateToSoundHistory

    /**
     * Call this immediately after calling `show()` on a toast.
     *
     * It will clear the toast request, so if the user rotates their phone it won't show a duplicate
     * toast.
     */
    fun doneShowingSnackbar() {
        _showSnackbarEvent.value = null
    }

    /**
     * Call this immediately after navigating to [SleepQualityFragment]
     *
     * It will clear the navigation request, so if the user rotates their phone it won't navigate
     * twice.
     */
    fun doneNavigating() {
        _navigateToSoundHistory.value = null
    }

    init {
        initializeLast()
    }

    private fun initializeLast() {
        viewModelScope.launch {
            last.value = getLastFromDatabase()
        }
    }

    /**
     *  Handling the case of the stopped app or forgotten recording,
     *  the start and end times will be the same.
     *
     *  If the start time and end time are not the same, then we do not have an unfinished
     *  recording.
     */
    private suspend fun getLastFromDatabase(): SoundHistory? {
        return database.getLast()
    }

    private suspend fun insert(history: SoundHistory) {
        database.insert(history)
    }

    private suspend fun update(history: SoundHistory) {
        database.update(history)
    }

    private suspend fun clear() {
        database.clear()
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