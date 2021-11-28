package com.example.acousticdoc.SoundHistory

import android.annotation.SuppressLint
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.acousticdoc.SoundHistory.SoundHistoryAdapter.ViewHolder.Companion.from
import com.example.acousticdoc.database.SoundHistory
import java.text.SimpleDateFormat

import android.R
import androidx.fragment.app.activityViewModels
import com.example.acousticdoc.ViewModel
import java.security.AccessController.getContext


class SoundHistoryAdapter: RecyclerView.Adapter<SoundHistoryAdapter.ViewHolder>() {

    var data =  listOf<SoundHistory>()
        set(value) {
            field = value
            notifyDataSetChanged()
        }

    override fun getItemCount() = data.size


    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val item = data[position]
        holder.bind(item)
    }


    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        return from(parent)
    }

    class ViewHolder private constructor(itemView: View) : RecyclerView.ViewHolder(itemView){
        val fullName: TextView = itemView.findViewById(AcousticDoc.R.id.FullName)
        val fileName: TextView = itemView.findViewById(AcousticDoc.R.id.FileName)
        val date: TextView = itemView.findViewById(AcousticDoc.R.id.Date)
        val diagnosis: TextView = itemView.findViewById(AcousticDoc.R.id.Diagnosis)

        fun bind(item: SoundHistory) {
            val res = itemView.context.resources
            fullName.text = item.firstName +" "+ item.lastName
            fileName.text = item.fileName
            date.text = item.date.toString()

        }

        companion object {
            fun from(parent: ViewGroup): ViewHolder {
                val layoutInflater = LayoutInflater.from(parent.context)
                val view = layoutInflater
                    .inflate(AcousticDoc.R.layout.list_item_sound_history, parent, false)

                return ViewHolder(view)
            }
        }
    }
    @SuppressLint("SimpleDateFormat")
    fun convertLongToDateString(systemTime: Long): String {
        return SimpleDateFormat("EEEE MMM-dd-yyyy' Time: 'HH:mm")
            .format(systemTime).toString()
    }
}