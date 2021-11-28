package com.example.acousticdoc.SoundHistory

import android.app.Application
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.acousticdoc.database.SoundHistoryDatabaseDao

/**
 * This is pretty much boiler plate code for a ViewModel Factory.
 *
 * Provides the SoundHistoryDatabaseDao and context to the ViewModel.
 */
class SoundHistoryViewModelFactory(
    private val dataSource: SoundHistoryDatabaseDao,
    private val application: Application) : ViewModelProvider.Factory {
    @Suppress("unchecked_cast")
    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        if (modelClass.isAssignableFrom(SoundHistoryViewModel::class.java)) {
            return SoundHistoryViewModel(dataSource, application) as T
        }
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}