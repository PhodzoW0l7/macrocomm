from datetime import datetime
from pydantic import BaseModel
from schemas.incidents import IncidentSeverity, IncidentStatus

class IncidentResponse(BaseModel):
    id:int
    vehicle_registration:str
    location:str
    issue_type:str
    description: str
    severity: IncidentSeverity
    status: IncidentStatus
    priority_score: int
    created_at: datetime