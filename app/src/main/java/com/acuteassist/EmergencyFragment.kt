package com.acuteassist

import android.os.Bundle
import android.view.*
import android.widget.*
import androidx.fragment.app.Fragment
import kotlinx.coroutines.*
import org.json.JSONArray
import org.json.JSONObject
import java.io.OutputStreamWriter
import java.net.HttpURLConnection
import java.net.URL

class EmergencyFragment : Fragment() {

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        return inflater.inflate(R.layout.activity_emergency, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val tvGuidance = view.findViewById<TextView>(R.id.tvAiGuidance)
        val etSymptoms = view.findViewById<EditText>(R.id.etSymptoms)
        val btnAnalyze = view.findViewById<Button>(R.id.btnAnalyze)
        val btnRefresh = view.findViewById<Button>(R.id.btnRefreshAi)

        // Medical history fetched from DB — hardcoded here for now
        val patientHistory = "Diabetes Type 2 (HbA1c 8.2%, Metformin 500mg), Hypertension (Amlodipine 5mg), Asthma (mild)"

        btnAnalyze.setOnClickListener {
            val symptoms = etSymptoms.text.toString()
            if (symptoms.isBlank()) {
                Toast.makeText(context, "Please enter symptoms", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            tvGuidance.text = "⏳ Analyzing with Ollama AI..."
            queryOllama(symptoms, patientHistory) { result ->
                activity?.runOnUiThread { tvGuidance.text = result }
            }
        }

        btnRefresh.setOnClickListener {
            tvGuidance.text = "⏳ Refreshing..."
            queryOllama("Patient appears confused and diaphoretic", patientHistory) { result ->
                activity?.runOnUiThread { tvGuidance.text = result }
            }
        }
    }

    /**
     * Queries local Ollama LLM running at http://10.0.2.2:11434 (localhost from emulator)
     * Model: llama3 or any medical model you have pulled
     * Replace with your actual Ollama server IP if running on device
     */
    private fun queryOllama(symptoms: String, history: String, callback: (String) -> Unit) {
        CoroutineScope(Dispatchers.IO).launch {
            try {
                val prompt = """
                    You are an emergency medical assistant AI.
                    Patient Medical History: $history
                    Current Symptoms: $symptoms
                    
                    Provide a numbered first-aid action list for the attending staff BEFORE the doctor arrives.
                    Include critical warnings based on the patient's history (drug interactions, contraindications).
                    Be concise. Max 8 steps. Use emoji bullets.
                """.trimIndent()

                val url = URL("http://10.0.2.2:11434/api/generate")
                val conn = url.openConnection() as HttpURLConnection
                conn.requestMethod = "POST"
                conn.setRequestProperty("Content-Type", "application/json")
                conn.doOutput = true

                val body = JSONObject().apply {
                    put("model", "llama3")
                    put("prompt", prompt)
                    put("stream", false)
                }.toString()

                OutputStreamWriter(conn.outputStream).use { it.write(body) }

                val response = conn.inputStream.bufferedReader().readText()
                val result = JSONObject(response).getString("response")
                callback(result)
            } catch (e: Exception) {
                callback("⚠️ Could not reach Ollama. Make sure it's running at localhost:11434\n\nError: ${e.message}")
            }
        }
    }
}