from pydantic import BaseModel

class TriageRequest(BaseModel):
    symptoms: str

class TriageResponse(BaseModel):
    diagnosis: str
    emergency_level: str
    immediate_action: str