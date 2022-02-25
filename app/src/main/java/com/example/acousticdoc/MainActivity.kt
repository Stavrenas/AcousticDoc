package com.example.acousticdoc

import AcousticDoc.R
import AcousticDoc.databinding.ActivityMainBinding
import android.Manifest
import android.app.AlertDialog
import android.content.ContextWrapper
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.navigateUp
import androidx.navigation.ui.setupActionBarWithNavController
import androidx.activity.result.contract.ActivityResultContracts
import android.content.DialogInterface
import android.os.Build
import android.os.Environment
import android.widget.Toast
import androidx.annotation.RequiresApi
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import java.io.File


class MainActivity : AppCompatActivity() {

    private lateinit var appBarConfiguration: AppBarConfiguration
    private lateinit var binding: ActivityMainBinding
    private val perms = arrayOf(Manifest.permission.RECORD_AUDIO, Manifest.permission.WRITE_EXTERNAL_STORAGE, Manifest.permission.READ_EXTERNAL_STORAGE)
    private val requestMultiplePermissions =  registerForActivityResult(ActivityResultContracts.RequestMultiplePermissions()) {}

    @RequiresApi(Build.VERSION_CODES.S)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)

        val navController = findNavController(R.id.nav_host_fragment_content_main)
        appBarConfiguration = AppBarConfiguration(navController.graph)
        setupActionBarWithNavController(navController, appBarConfiguration)

        //Create files folder if it does not exist
        val cw = ContextWrapper(this)
        val path = cw.getExternalFilesDir(null)

        if (path != null) {
            if(!path.exists()){
                path.mkdirs()
            }
        }

        //Request all permissions
        requestMultiplePermissions.launch(perms)

        //Start python
        if (! Python.isStarted()) {
            Python.start( AndroidPlatform(this))
        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Inflate the menu; this adds items to the action bar if it is present.
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle action bar item clicks.
        return when (item.itemId) {
            R.id.action_about -> {
                AlertDialog.Builder(this)
                    .setTitle("Σχετικά με μας :)")
                    .setMessage("Αυτή η εφαρμογή είναι κομμάτι της εργασίας μας στο μάθημα \"Τεχνολογία Ήχου και Εικόνας\" .\nΦοιτητές :\nΣταύρος Μαλακούδης samalako@[ECE]\nΚαραγκιοζίδης Νίκος karagkio@[ECE]\nΑγγέλου Ανδρέας aangelou@[ECE]\nΜπούγιας Νίκος nmpougias@[ECE]\nΤσακιρίδης Γιώργος tsakgeor@[ECE]\n[ECE]=ece.auth.gr")
                    .setPositiveButton("Τέλεια!", null)
                    .show()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    override fun onSupportNavigateUp(): Boolean {
        val navController = findNavController(R.id.nav_host_fragment_content_main)
        return navController.navigateUp(appBarConfiguration)
                || super.onSupportNavigateUp()
    }

}