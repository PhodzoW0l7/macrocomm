from pydantic import BaseModel
from backend.schemas.incidents import IncidentStatus

class IncidentStatusUpdateRequest(BaseModel):
    status: IncidentStatus
