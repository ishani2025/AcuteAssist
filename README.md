# CardioAid
AcuteAssist – AI‑Powered Emergency Triage System
AcuteAssist is an AI-assisted medical triage system that analyzes patient symptoms and generates structured emergency recommendations using Retrieval-Augmented Generation (RAG).

The system integrates a vector medical knowledge base with a medical language model to assist in identifying possible emergency conditions and prioritizing care.

Problem Statement
Emergency departments often face high patient loads and limited medical staff, which can delay the identification of critical conditions.

Patients presenting symptoms such as chest pain, breathing difficulty, or neurological symptoms require rapid assessment to determine the urgency of medical attention.

However:

Initial triage can be time‑consuming

Symptoms may be ambiguous or overlapping

Early identification of life‑threatening conditions is critical

There is a need for an AI-assisted triage system that can quickly analyze symptoms and suggest possible diagnoses with urgency levels.

Proposed Solution
AcuteAssist provides an AI-driven triage assistant that:

Accepts patient symptoms from a mobile application.

Retrieves relevant medical knowledge using vector search.

Uses a medical language model to analyze symptoms.

Returns a structured triage recommendation including:

Diagnosis

Emergency severity level

Immediate action

This helps prioritize critical cases while identifying non-emergency conditions, assisting healthcare workers in faster decision-making.

Demo Cases
Case 1 – Cardiac Emergency
Input Symptoms:

chest pain sweating nausea left arm pain
Output:

Diagnosis: Acute Myocardial Infarction
Emergency_Level: CRITICAL
Immediate_Action: Call emergency services immediately.
Explanation:
The system recognizes classic heart attack symptoms and prioritizes the case as CRITICAL.

Case 2 – Mild Respiratory Illness
Input Symptoms:

runny nose mild cough sore throat
Output:

Diagnosis: Upper Respiratory Infection
Emergency_Level: LOW
Immediate_Action: Rest, hydration, and monitor symptoms.
Explanation:
The system identifies a non‑emergency illness, avoiding unnecessary escalation.

System Workflow
User enters symptoms in Android App
              ↓
Request sent to FastAPI Backend
              ↓
Redis Cache checks for repeated queries
              ↓
RAG Pipeline retrieves medical knowledge
              ↓
ChromaDB vector database finds relevant chunks
              ↓
BioMistral medical LLM analyzes symptoms
              ↓
Structured triage recommendation generated
              ↓
Response sent back to Android App
Project Architecture
Android Mobile App
        ↓
FastAPI Backend
        ↓
Redis Cache
        ↓
RAG Retrieval Pipeline
        ↓
ChromaDB Vector Knowledge Base
        ↓
BioMistral Medical LLM (Ollama)
        ↓
Emergency Triage Response
Tech Stack
Frontend
Android Studio

Kotlin / Java

REST API integration

Backend
Python

FastAPI

Uvicorn

AI / Machine Learning
BioMistral Medical LLM

Ollama (local LLM inference)

Retrieval-Augmented Generation (RAG)

Data Layer
ChromaDB (vector database)

Redis (caching layer)

Development Tools
Git & GitHub

Python virtual environments

Key Features
AI-assisted symptom analysis

Retrieval-Augmented Generation (RAG) for medical reasoning

Vector-based medical knowledge retrieval

Structured triage output format

Caching for faster responses

Scalable architecture for integration with healthcare applications

Disclaimer
This project is designed for educational and research purposes only and does not replace professional medical diagnosis or treatment.

If you want, I can also give you a much stronger README version that can help you score higher on the hackathon evaluation criteria (judges often look for specific wording).


Show more







with good space which i can copy paste directly

ChatGPT10:39 AM
Here is a clean, well‑spaced README that you can copy‑paste directly into GitHub.

AcuteAssist – AI‑Powered Emergency Triage System
AcuteAssist is an AI‑assisted emergency triage system designed to analyze patient symptoms and provide structured medical recommendations using Retrieval‑Augmented Generation (RAG).

The system integrates a vector medical knowledge base with a medical language model to assist in identifying possible emergency conditions and prioritizing patient care.

Problem Statement
Emergency departments frequently face high patient volumes and limited medical staff, making rapid triage essential for identifying life‑threatening conditions.

Patients presenting symptoms such as chest pain, breathing difficulty, or neurological issues require quick evaluation to determine the urgency of treatment.

However:

Initial triage is often time‑consuming

Symptoms can be ambiguous or overlapping

Delays in recognizing critical conditions can impact patient outcomes

There is a need for an AI‑assisted system that can quickly analyze symptoms and provide structured triage recommendations to support healthcare professionals.

Proposed Solution
AcuteAssist provides an AI-driven triage assistant that helps identify potential medical emergencies.

The system:

Accepts patient symptoms from a mobile application.

Retrieves relevant medical knowledge using vector search.

Uses a medical language model to analyze symptoms.

Generates a structured triage response including:

Diagnosis

Emergency severity level

Immediate recommended action.

This helps prioritize critical cases while identifying non-emergency conditions, assisting healthcare staff in faster decision-making.

Demo Cases
Case 1 – Cardiac Emergency
Input Symptoms

chest pain sweating nausea left arm pain
Output

Diagnosis: Acute Myocardial Infarction
Emergency_Level: CRITICAL
Immediate_Action: Call emergency services immediately.
Explanation

The system recognizes classic heart attack symptoms and prioritizes the case as CRITICAL, recommending immediate medical attention.

Case 2 – Mild Respiratory Illness
Input Symptoms

runny nose mild cough sore throat
Output

Diagnosis: Upper Respiratory Infection
Emergency_Level: LOW
Immediate_Action: Rest, hydration, and monitor symptoms.
Explanation

The system identifies a non‑emergency condition and provides basic care guidance without unnecessary escalation.

System Workflow
User enters symptoms in the Android application
                ↓
Request sent to FastAPI backend
                ↓
Redis cache checks for repeated queries
                ↓
RAG pipeline retrieves relevant medical knowledge
                ↓
ChromaDB vector database finds similar symptom contexts
                ↓
BioMistral medical LLM analyzes symptoms and knowledge
                ↓
Structured triage recommendation generated
                ↓
Response returned to the Android application
Project Architecture
Android Mobile App
        ↓
FastAPI Backend
        ↓
Redis Cache Layer
        ↓
RAG Retrieval Pipeline
        ↓
ChromaDB Vector Database
        ↓
BioMistral Medical LLM (via Ollama)
        ↓
Structured Emergency Triage Response
Tech Stack
Frontend
Android Studio

Kotlin / Java

REST API Integration

Backend
Python

FastAPI

Uvicorn

AI / Machine Learning
BioMistral Medical Language Model

Ollama (Local LLM Inference)

Retrieval‑Augmented Generation (RAG)

Data Layer
ChromaDB (Vector Database for medical knowledge retrieval)

Redis (Caching layer for faster repeated queries)

Development Tools
Git & GitHub

Python Virtual Environment

Key Features
AI‑assisted symptom analysis

Retrieval‑Augmented Generation (RAG) for medical reasoning

Vector-based medical knowledge retrieval

Structured triage output format

Redis caching for faster responses

Modular and scalable architecture

Disclaimer
This project is intended for educational and research purposes only.

It does not replace professional medical diagnosis or treatment and should not be used as a substitute for consultation with qualified healthcare professionals.
