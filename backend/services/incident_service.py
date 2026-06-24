class IncidentService:
    def list_incidents(self) -> list:
        return []

    def create_incident(self, request) -> dict:
        # Placeholder implementation
        return {"detail": "Not implemented"}

    def update_status(self, incident_id: int, status: str):
        # Placeholder: return None to indicate not found
        return None

    def get_summary(self) -> dict:
        by_status = {"new": 0, "assigned": 0, "in_progress": 0, "resolved": 0}
        by_severity = {"low": 0, "medium": 0, "high": 0, "critical": 0}
        return {"total": 0, "by_status": by_status, "by_severity": by_severity}


def get_incident_service() -> IncidentService:
    return IncidentService()
