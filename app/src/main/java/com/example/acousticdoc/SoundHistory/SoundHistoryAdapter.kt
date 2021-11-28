package com.example.acousticdoc.SoundHistory

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.acousticdoc.SoundHistory.SoundHistoryAdapter.ViewHolder.Companion.from
import com.example.acousticdoc.database.SoundHistory


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
            date.text = getDateFromInt(item.date)
            diagnosis.text = item.diagnosis

        }

        companion object {
            fun from(parent: ViewGroup): ViewHolder {
                val layoutInflater = LayoutInflater.from(parent.context)
                val view = layoutInflater
                    .inflate(AcousticDoc.R.layout.list_item_sound_history, parent, false)

                return ViewHolder(view)
            }
        }
        fun getDateFromInt(date: Long): String {
            val str = date.toString()
            return "" + str[0] + str[1] + "/" + str[2] + str[3] + "/" + str[4] + str[5] + str[6] + str[7] +
                    "-" + str[8] + str[9] + ":" + str[10] + str[11]
        }
    }


}