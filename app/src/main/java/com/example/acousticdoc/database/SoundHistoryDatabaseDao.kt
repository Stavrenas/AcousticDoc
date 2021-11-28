package com.example.acousticdoc.database


import androidx.lifecycle.LiveData
import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update


/**
 * Defines methods for using the SleepNight class with Room.
 */
@Dao
interface SoundHistoryDatabaseDao{

    @Insert
    fun insert(history: SoundHistory)

    /**
     * When updating a row with a value already set in a column,
     * replaces the old value with the new one.
     *
     *
     */
    @Update
    fun update(history: SoundHistory)

    /**
     * Selects and returns the row that matches the supplied key.
     *
     * @param key startTimeMilli to match
     */
    @Query("SELECT * from sound_history_table WHERE historyID = :key")
    fun get(key: Long): SoundHistory

//    /**
//     * Deletes all values from the table.
//     *
//     * This does not delete the table, only its contents.
//     */
//    @Query("DELETE FROM sound_history_table")
//    suspend fun clear()

    /**
     * Selects and returns all rows in the table,
     *
     * sorted by start time in descending order.
     */
    @Query("SELECT * FROM sound_history_table ORDER BY historyID DESC")
    fun getAllHistory(): LiveData<List<SoundHistory>>?

    /**
     * Selects and returns the latest night.
     */
    @Query("SELECT * FROM sound_history_table ORDER BY historyID DESC LIMIT 1")
    fun getLast(): SoundHistory?
}