package com.example.acousticdoc.database
import androidx.lifecycle.LiveData
import android.app.Application
import com.example.acousticdoc.database.SoundHistory
import com.example.acousticdoc.database.SoundHistoryDatabase
import com.example.acousticdoc.database.SoundHistoryDatabaseDao


class SoundHistoryRepository {
    private var mSoundHistoryDatabaseDao: SoundHistoryDatabaseDao? = null
    private var mAllHistory: LiveData<List<SoundHistory?>?>? = null

    // Note that in order to unit test the WordRepository, you have to remove the Application
    // dependency. This adds complexity and much more code, and this sample is not about testing.
    // See the BasicSample in the android-architecture-components repository at
    // https://github.com/googlesamples
    fun WordRepository(application: Application?) {
        val db: SoundHistoryDatabase = SoundHistoryDatabase.getDatabase(application)
        mSoundHistoryDatabaseDao = db.soundHistoryDatabaseDao()
        mAllHistory = mSoundHistoryDatabaseDao.getAllHistory()
    }

    // Room executes all queries on a separate thread.
    // Observed LiveData will notify the observer when the data has changed.
    fun AllHistory(): LiveData<List<SoundHistory?>?>? {
        return mAllHistory
    }

    // You must call this on a non-UI thread or your app will throw an exception. Room ensures
    // that you're not doing any long running operations on the main thread, blocking the UI.
    fun insert(hist: SoundHistory?) {
        WordRoomDatabase.databaseWriteExecutor.execute {
            if (hist != null) {
                mSoundHistoryDatabaseDao?.insert(hist)
            }
        }
    }
}