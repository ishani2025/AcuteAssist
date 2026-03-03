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
