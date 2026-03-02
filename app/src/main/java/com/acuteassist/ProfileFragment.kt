package com.acuteassist

import android.os.Bundle
import android.view.*
import android.widget.*
import androidx.fragment.app.Fragment

class ProfileFragment : Fragment() {

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        return inflater.inflate(R.layout.activity_profile, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        view.findViewById<Button>(R.id.btnSignOut)?.setOnClickListener {
            requireActivity().finish()
            startActivity(android.content.Intent(requireContext(), LoginActivity::class.java))
        }
    }
}