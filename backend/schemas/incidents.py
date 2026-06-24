from enum import Enum


class IncidentSeverity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"

class IncidentStatus(str, Enum):
    new = "new"
    assigned = "assigned"
    in_progress = "in_progress"
    resolved = "resolved"