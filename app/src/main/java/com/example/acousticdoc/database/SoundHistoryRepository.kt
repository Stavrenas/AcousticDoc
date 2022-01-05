package com.example.acousticdoc.database
import androidx.lifecycle.LiveData
import androidx.annotation.WorkerThread
import com.example.acousticdoc.database.SoundHistoryDatabaseDao


class SoundHistoryRepository(private val SoundDao: SoundHistoryDatabaseDao) {
    var allHistory: LiveData<List<SoundHistory>>? = SoundDao.getAllHistory()

    @Suppress("RedundantSuspendModifier")
    @WorkerThread
    suspend fun insert(hist: SoundHistory) {
        SoundDao.insert(hist)
    }
}