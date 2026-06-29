from fastapi import Depends, APIRouter, HTTPException
# Response models currently not available; omitting response_model to avoid import errors
from models.IncidentResponse import IncidentResponse
from services import incident_service

incidentRouter = APIRouter()


@incidentRouter.get("/health")
def get_apihealth():
    return {"status": "ok","message": "Fleet Rescue API is running"}

#get request for incidents method/function
@incidentRouter.get("/incidents", response_model=list[IncidentResponse])
def get_incidents(service:incident_service = Depends(incident_service.get_incident_service)):
    return service.list_incidents()

#post reuqest for incidents function/method
@incidentRouter.post("/incidents", response_model=IncidentResponse)
def create_incident(
    request,
    service:incident_service.IncidentService=Depends(incident_service.get_incident_service)):
    return service.list_incidents()

#update function/method
@incidentRouter.patch("/incidents/{incident_id}/status", response_model=list[IncidentResponse])
def update_incident_status(
    incident_id:int,
    request,
    service:incident_service.IncidentService=Depends(incident_service.get_incident_service),
    ):
    incident=service.update_status(incident_id,request.status)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return service.list_incidents()

@incidentRouter.get("/summary")
def get_incident_summary(service: incident_service.IncidentService =
                        Depends(incident_service.get_incident_service)):
    return service.get_summary()