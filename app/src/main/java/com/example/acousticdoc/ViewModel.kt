package com.example.acousticdoc

import android.net.Uri
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel


class ViewModel : ViewModel() {
    private val _uri = MutableLiveData<Uri>()
    val uri: LiveData<Uri> = _uri

    private val _title= MutableLiveData<String>()
    val title: LiveData<String> = _title


    fun setModelUri(targetUri: Uri){
        _uri.value = targetUri
    }

    fun getModelUri() : Uri? {
        return  _uri.value
    }


    fun setTitleValue(str: String){
        _title.value = str
    }


    fun getTitleValue(): String? {
        return _title.value
    }

}

//@BindingAdapter("resource")
//fun setSoundUri(view: ImageView, sound: Uri) {
//    view.setImageURI(sound)
//}



