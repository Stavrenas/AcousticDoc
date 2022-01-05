package com.example.acousticdoc.SoundHistory

import android.app.Application
import androidx.lifecycle.*
import com.example.acousticdoc.database.SoundHistoryDatabaseDao
import com.example.acousticdoc.database.SoundHistory
import com.example.acousticdoc.database.SoundHistoryRepository
import kotlinx.coroutines.launch

class SoundHistoryViewModel (private val repository: SoundHistoryRepository
) : ViewModel() {

    val allHistory: LiveData<List<SoundHistory>>? = repository.allHistory

    fun insert(history: SoundHistory) = viewModelScope.launch {
        repository.insert(history)
    }

}

class SoundHistoryViewModelFactory(private val repository: SoundHistoryRepository) : ViewModelProvider.Factory {
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        if (modelClass.isAssignableFrom(SoundHistoryViewModel::class.java)) {
            @Suppress("UNCHECKED_CAST")
            return SoundHistoryViewModel(repository) as T
        }
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}


