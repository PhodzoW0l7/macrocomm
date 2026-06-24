from fastapi import Depends, APIRouter, HTTPException
# Response models currently not available; omitting response_model to avoid import errors
from services import incident_service

incidentRouter = APIRouter()

MOCK_INCIDENTS = [
    {
        "id": 1,
        "vehicle_id": "VHC-789-GP",
        "location": "N1 Highway, Midrand",
        "issue": "Engine Overheating & Coolant Leak",
        "severity": "critical",
        "status": "in_progress",
        "priority": "High"
    },
    {
        "id": 2,
        "vehicle_id": "VHC-432-WP",
        "location": "R21, Near OR Tambo",
        "issue": "Flat Tyre / Damaged Rim",
        "severity": "low",
        "status": "new",
        "priority": "Low"
    }
]

@incidentRouter.get("/health")
def get_apihealth():
    return {"status": "ok", "message": "Fleet Rescue API is running"}

# get request for incidents method/function
@incidentRouter.get("/incidents")
def get_incidents():
    # Returning the mock list directly for testing
    return MOCK_INCIDENTS

# post request for incidents function/method
@incidentRouter.post("/incidents")
def create_incident(request):
    # Simulates adding data by returning the dataset
    return MOCK_INCIDENTS

# update function/method
@incidentRouter.patch("/incidents/{incident_id}/status")
def update_incident_status(incident_id: int, request):
    # Find mock item and simulate modification
    for incident in MOCK_INCIDENTS:
        if incident["id"] == incident_id:
            incident["status"] = getattr(request, "status", "assigned")
            return MOCK_INCIDENTS
    raise HTTPException(status_code=404, detail="Incident not found")

@incidentRouter.get("/summary")
def get_incident_summary():
    # 2. Match summary keys expected by Angular metrics view (.total, .new, etc.)
    total = len(MOCK_INCIDENTS)
    new_count = sum(1 for i in MOCK_INCIDENTS if i["status"] == "new")
    assigned_count = sum(1 for i in MOCK_INCIDENTS if i["status"] == "assigned")
    progress_count = sum(1 for i in MOCK_INCIDENTS if i["status"] == "in_progress")
    resolved_count = sum(1 for i in MOCK_INCIDENTS if i["status"] == "resolved")

    return {
        "total": total,
        "new": new_count,
        "assigned": assigned_count,
        "in_progress": progress_count,
        "resolved": resolved_count
    }