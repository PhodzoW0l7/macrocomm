from pydantic import BaseModel, Field
from backend.schemas.incidents import IncidentSeverity

class IncidentCreateRequest(BaseModel):
    vehicle_registration: str = Field(min_length=3, max_length=20)
    location: str = Field(min_length=3)
    issue_type: str = Field(min_length=3)
    description: str = Field(min_length=5)
    severity: IncidentSeverity