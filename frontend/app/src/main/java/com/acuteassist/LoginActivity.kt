package com.acuteassist

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class LoginActivity : AppCompatActivity() {

    private var selectedRole = "Doctor"
    private lateinit var checkDoctor: TextView
    private lateinit var checkNurse: TextView
    private lateinit var checkAdmin: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        checkDoctor = findViewById(R.id.checkDoctor)
        checkNurse = findViewById(R.id.checkNurse)
        checkAdmin = findViewById(R.id.checkAdmin)

        // Default: Doctor selected
        checkDoctor.visibility = View.VISIBLE

        setupRoleSelection()

        findViewById<Button>(R.id.btnSignIn).setOnClickListener {
            val intent = Intent(this, MainActivity::class.java)
            intent.putExtra("role", selectedRole)
            startActivity(intent)
        }
    }

    private fun setupRoleSelection() {
        val roleDoctor = findViewById<LinearLayout>(R.id.roleDoctor)
        val roleNurse = findViewById<LinearLayout>(R.id.roleNurse)
        val roleAdmin = findViewById<LinearLayout>(R.id.roleAdmin)

        roleDoctor.setOnClickListener { selectRole("Doctor") }
        roleNurse.setOnClickListener { selectRole("Nurse") }
        roleAdmin.setOnClickListener { selectRole("Admin") }
    }

    private fun selectRole(role: String) {
        selectedRole = role
        checkDoctor.visibility = if (role == "Doctor") View.VISIBLE else View.INVISIBLE
        checkNurse.visibility = if (role == "Nurse") View.VISIBLE else View.INVISIBLE
        checkAdmin.visibility = if (role == "Admin") View.VISIBLE else View.INVISIBLE
    }
}