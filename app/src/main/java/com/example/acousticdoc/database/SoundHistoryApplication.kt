package com.example.acousticdoc.database

import android.app.Application

class SoundHistoryApplication: Application() {
    val database by lazy { SoundHistoryDatabase.getDatabase(this) }
    val repository by lazy { SoundHistoryRepository(database.soundHistoryDatabaseDao()) }
}