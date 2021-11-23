package com.example.acousticdoc.SoundHistory

import android.app.Application
import androidx.lifecycle.*
import com.example.acousticdoc.database.HistoryDatabaseDao
import com.example.acousticdoc.database.SoundHistory
import kotlinx.coroutines.launch

class SoundHistoryViewModel ( dataSource: HistoryDatabaseDao,
application: Application
) : ViewModel() {

    /**
     * Hold a reference to SleepDatabase via SleepDatabaseDao.
     */
    val database = dataSource


    private var last = MutableLiveData<SoundHistory?>()

    val nights = database.getAllHistory()

    /**
     * Converted nights to Spanned for displaying.
     */
    val nightsString = Transformations.map(nights) { nights ->
        formatNights(nights, application.resources)
    }

    /**
     * If tonight has not been set, then the START button should be visible.
     */
    val startButtonVisible = Transformations.map(last) {
        null == it
    }

    /**
     * If tonight has been set, then the STOP button should be visible.
     */
    val stopButtonVisible = Transformations.map(last) {
        null != it
    }

    /**
     * If there are any nights in the database, show the CLEAR button.
     */
    val clearButtonVisible = Transformations.map(nights) {
        it?.isNotEmpty()
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
    private val _navigateToSleepQuality = MutableLiveData<SoundHistory>()

    /**
     * If this is non-null, immediately navigate to [SleepQualityFragment] and call [doneNavigating]
     */
    val navigateToSleepQuality: LiveData<SoundHistory>
    get() = _navigateToSleepQuality

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
        _navigateToSleepQuality.value = null
    }

    init {
        initializeTonight()
    }

    private fun initializeTonight() {
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
        var night = database.getLast()
        if (night?.endTimeMilli != night?.startTimeMilli) {
            night = null
        }
        return night
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

    /**
     * Executes when the START button is clicked.
     */
    fun onStart() {
        viewModelScope.launch {
            // Create a new night, which captures the current time,
            // and insert it into the database.
            val newHistory = SoundHistory()

            insert(newHistory)

            last.value = getTonightFromDatabase()
        }
    }

    /**
     * Executes when the STOP button is clicked.
     */
    fun onStop() {
        viewModelScope.launch {
            // In Kotlin, the return@label syntax is used for specifying which function among
            // several nested ones this statement returns from.
            // In this case, we are specifying to return from launch().
            val oldNight = last.value ?: return@launch

            // Update the night in the database to add the end time.
            oldNight.endTimeMilli = System.currentTimeMillis()

            update(oldNight)

            // Set state to navigate to the SleepQualityFragment.
            _navigateToSleepQuality.value = oldNight
        }
    }

    /**
     * Executes when the CLEAR button is clicked.
     */
    fun onClear() {
        viewModelScope.launch {
            // Clear the database table.
            clear()

            // And clear tonight since it's no longer in the database
            last.value = null

            // Show a snackbar message, because it's friendly.
            _showSnackbarEvent.value = true
        }
    }
}