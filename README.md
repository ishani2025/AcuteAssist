# CardioAid
# AcuteAssist

AcuteAssist is an AI-assisted emergency triage system for government and NGO-run hospitals. It is designed to help doctors on emergency duty generate a short, relevant clinical summary from a patient’s symptoms, past history, and retrieved medical knowledge so they can act faster with less noise.

The main idea is simple:

1. take the patient’s current symptoms,
2. retrieve only the most relevant medical context,
3. send a compact prompt to a local LLM,
4. return a structured triage response.

This reduces unnecessary token usage and keeps the workflow more cost-efficient for low-budget healthcare settings.

---

## What the project currently does

The repository currently contains:

- an **Android app** built with Kotlin
- a **FastAPI backend**
- a **SQLite database**
- a **ChromaDB knowledge base** for medical retrieval
- a **local Ollama model** for triage generation
- basic **patient, hospital, user, test, and audit** data models
- initial scaffolding for **role-based access**, **Redis caching**, and **fragmented hospital history**

---

## Core workflow

### Current triage flow
- The doctor enters symptoms in the Android app.
- The app sends a request to the backend endpoint `POST /ai-triage`.
- The backend retrieves relevant medical context from ChromaDB.
- The backend sends the symptoms plus retrieved context to a local LLM through Ollama.
- The LLM returns a structured response with:
  - `diagnosis`
  - `emergency_level`
  - `immediate_action`

### Data flow in the repository
- **Android app**: captures symptoms and displays the triage result
- **FastAPI backend**: handles API requests
- **SQLite**: stores patients, hospitals, medical tests, and users
- **ChromaDB**: stores medical knowledge chunks
- **Ollama**: runs the local model used for triage generation

---

## Key features implemented so far

### 1. Android emergency triage UI
The app includes:
- login screen
- patient screen
- emergency triage screen
- profile screen

### 2. Backend triage endpoint
The backend exposes an AI triage API that:
- accepts symptom text
- retrieves related medical knowledge
- generates a concise emergency response

### 3. Medical data model
The backend already defines models for:
- patients
- hospitals
- patient-hospital links
- medical tests
- audit logs
- users

### 4. Knowledge retrieval pipeline
The repository includes scripts and services for:
- PDF text extraction
- text cleaning
- chunking medical text
- loading chunks into ChromaDB
- retrieving top relevant chunks for a symptom query

### 5. Early cost-control idea
The project reduces prompt size by:
- cleaning extracted text
- selecting only relevant chunks
- keeping the LLM prompt short and structured

---

## Repository structure

```text
AcuteAssist/
├── backend/
│   ├── app/
│   ├── api/routes/
│   ├── auth/
│   ├── database/
│   ├── data/
│   ├── models/
│   ├── services/
│   └── tests/
└── frontend/
    └── app/
```

---

## Backend components

### API routes
- `auth_routes.py` — user registration and login
- `patient_routes.py` — patient creation and listing
- `hospital_routes.py` — hospital creation and linking
- `test_routes.py` — medical test entry
- `triage_routes.py` — triage by patient id
- `ai_routes.py` — direct symptom-based AI triage

### Services
- `rag_pipeline.py` — retrieval + LLM triage pipeline
- `retrieval_service.py` — fetches relevant knowledge from ChromaDB
- `llm_service.py` — sends prompts to Ollama
- `pdf_extraction.py` — extracts text from PDFs
- `chunking.py` — splits text into chunks
- `cleaning_service.py` — cleans extracted text
- `deterministic_filter.py` — extracts clinical markers from tests
- `triage_service.py` — combines patient data, history, and retrieval logic
- `redis_services.py` — basic Redis cache helpers

### Database
- `db.py` — SQLAlchemy setup using SQLite
- `models.py` — database tables
- repository files for patients, hospitals, users, tests, and audit logs

---

## Android app screens

### Login
The login screen lets the user pick a role:
- Doctor
- Nurse
- Admin

### Patient screen
This screen currently shows a set of sample patient conditions and toggles. It is a prototype for medical history selection.

### Emergency screen
This screen accepts symptoms and sends them to the backend triage API.

### Profile screen
Basic sign-out flow.

---

## Tech stack

### Frontend
- Kotlin
- Android Studio
- AndroidX
- Coroutines
- Fragment-based UI

### Backend
- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

### AI / retrieval
- Ollama
- ChromaDB
- Sentence Transformers
- Retrieval-Augmented Generation

### Storage / support
- SQLite
- Redis scaffolding

---

## Setup

## Backend

From the `backend/` directory:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Notes:
- The backend currently uses SQLite: `sqlite:///./acuteassist.db`
- Ollama must be running locally for the model call to work
- ChromaDB must contain the `medical_knowledge` collection for retrieval to succeed

### Knowledge base loading
The repository includes scripts under `backend/data/scripts/` to prepare and load knowledge chunks into ChromaDB.

---

## Android

Open the `frontend/` folder in Android Studio and run the app on an emulator or device.

The emergency screen currently calls:

```text
http://10.0.2.2:8000/ai-triage
```

`10.0.2.2` is used so the Android emulator can reach the local machine.

---

## API endpoints in the current code

### Auth
- `POST /auth/register`
- `POST /auth/login`

### Patients
- `POST /patients/`
- `GET /patients/`
- `GET /patients/{patient_id}`

### Hospitals
- `POST /hospitals/`
- `GET /hospitals/`
- `POST /hospitals/link/`

### Medical tests
- `POST /medical-tests/`

### Triage
- `POST /ai-triage`
- `POST /triage/{patient_id}`

---

## Current limitations

This repository is still in prototype stage.

Some modules are present as scaffolding and are not fully wired into the main runtime yet, including:
- Redis caching in the request path
- fragmented history fetch logic
- some hospital-specific service files
- embedding and risk engine placeholders

The main triage idea is implemented, but the production workflow still needs cleanup before deployment.

---

## Disclaimer

AcuteAssist is intended for educational and prototype use only. It does not replace professional clinical judgment, emergency protocols, or formal medical diagnosis.

---

## Suggested next step

The next logical upgrade is to connect:
- authenticated users
- real patient history-->Integrate with UHID and ABHA
- cached retrieval
- structured triage output
- proper role-based access control
- Given the option to upload patient current medical tests files.
into one clean production flow.
