package com.example.acousticdoc.database

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey
import java.sql.Date


@Entity(tableName = "sound_history_table")
data class SoundHistory(
    @PrimaryKey(autoGenerate = true)
    var historyID: Long = 0L,

    @ColumnInfo(name = "date")
    val date: Date = Date(2020,1,1),

    @ColumnInfo(name = "name")
    var firstName: String = "",

    @ColumnInfo(name = "lastName")
    var lastName: String = "",

    @ColumnInfo(name = "diagnosis")
    var diagnosis: String = "",

    @ColumnInfo(name = "fileName")
    var fileName: String = "")