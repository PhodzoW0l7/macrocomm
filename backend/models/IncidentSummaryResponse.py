from pydantic import BaseModel

class IncidentSummaryResponse(BaseModel):
    total:int
    by_status:dict[str,int]
    by_severity:dict[str,int]
    