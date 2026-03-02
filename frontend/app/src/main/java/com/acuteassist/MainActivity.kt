package com.acuteassist

import android.content.Intent
import com.acuteassist.R
import android.os.Bundle
import android.widget.LinearLayout
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment

class MainActivity : AppCompatActivity() {

    private lateinit var navPatientLabel: TextView
    private lateinit var navProfileLabel: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        navPatientLabel = findViewById(R.id.navPatientLabel)
        navProfileLabel = findViewById(R.id.navProfileLabel)

        // Default screen
        loadFragment(PatientFragment())

        findViewById<LinearLayout>(R.id.navPatient).setOnClickListener {
            loadFragment(PatientFragment())
            updateNavColors(active = "patient")
        }

        findViewById<LinearLayout>(R.id.navEmergency).setOnClickListener {
            loadFragment(EmergencyFragment())
            updateNavColors(active = "emergency")
        }

        findViewById<LinearLayout>(R.id.navProfile).setOnClickListener {
            loadFragment(ProfileFragment())
            updateNavColors(active = "profile")
        }
    }

    private fun loadFragment(fragment: Fragment) {
        supportFragmentManager.beginTransaction()
            .replace(R.id.fragmentContainer, fragment)
            .commit()
    }

    private fun updateNavColors(active: String) {
        navPatientLabel.setTextColor(getColor(if (active == "patient") R.color.accent else R.color.text_muted))
        navProfileLabel.setTextColor(getColor(if (active == "profile") R.color.accent else R.color.text_muted))
    }
}