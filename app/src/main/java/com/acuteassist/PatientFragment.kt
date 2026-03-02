package com.acuteassist

import android.graphics.Color
import android.os.Bundle
import android.view.*
import android.widget.*
import androidx.fragment.app.Fragment

class PatientFragment : Fragment() {

    data class Condition(val name: String, val comment: String?, var isOn: Boolean)

    private val conditions = listOf(
        Condition("Diabetes (Type 2)", "HbA1c 8.2% — On Metformin 500mg BD. Monitor fasting glucose daily.", true),
        Condition("Hypertension", "BP usually 150/95 — Amlodipine 5mg OD. Low-salt diet advised.", true),
        Condition("Heart Disease", null, false),
        Condition("Stroke History", null, false),
        Condition("Epilepsy", null, false),
        Condition("Asthma", "Mild intermittent — Salbutamol inhaler PRN. Avoid dust/allergens.", true),
    )

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        return inflater.inflate(R.layout.activity_patient, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        buildConditions(view)
        buildInfoRows(view)
    }

    private fun buildInfoRows(view: View) {
        val container = view.findViewById<LinearLayout>(R.id.conditionsContainer) ?: return
        // You can add static info rows for basic info card here
        // or use a RecyclerView for scalability
    }

    private fun buildConditions(view: View) {
        val container = view.findViewById<LinearLayout>(R.id.conditionsContainer) ?: return
        container.removeAllViews()

        conditions.forEach { condition ->
            val rowLayout = LinearLayout(requireContext()).apply {
                orientation = LinearLayout.HORIZONTAL
                gravity = android.view.Gravity.CENTER_VERTICAL
                setPadding(0, 20, 0, 20)
            }

            val infoLayout = LinearLayout(requireContext()).apply {
                orientation = LinearLayout.VERTICAL
                layoutParams = LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT, 1f)
            }

            val nameView = TextView(requireContext()).apply {
                text = condition.name
                textSize = 13f
                setTextColor(Color.parseColor("#E8EDF5"))
            }
            infoLayout.addView(nameView)

            val commentView = condition.comment?.let {
                TextView(requireContext()).apply {
                    text = it
                    textSize = 11f
                    setTextColor(Color.parseColor("#6B7FA3"))
                    visibility = if (condition.isOn) View.VISIBLE else View.GONE
                    setPadding(16, 8, 0, 8)
                }
            }
            commentView?.let { infoLayout.addView(it) }

            val toggle = Switch(requireContext()).apply {
                isChecked = condition.isOn
                setOnCheckedChangeListener { _, isChecked ->
                    condition.isOn = isChecked
                    commentView?.visibility = if (isChecked) View.VISIBLE else View.GONE
                }
            }

            rowLayout.addView(infoLayout)
            rowLayout.addView(toggle)
            container.addView(rowLayout)

            // Divider
            val divider = View(requireContext()).apply {
                layoutParams = LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT, 1
                )
                setBackgroundColor(Color.parseColor("#1F2D45"))
            }
            container.addView(divider)
        }
    }
}