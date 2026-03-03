from sqlalchemy.orm import Session
from database.models import AuditLog
from datetime import datetime
import uuid

def create_audit_log(db: Session, user_role: str, action_type: str, patient_id: str = None):
    log = AuditLog(
        id=str(uuid.uuid4()),
        user_role=user_role,
        action_type=action_type,
        patient_id=patient_id,
        timestamp=datetime.utcnow()
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
