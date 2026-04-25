from enum import Enum

class Sex(str, Enum):
    FEMALE = "female"
    MALE = "male"

class AgeUnit(str, Enum):
    DAY = "day"
    MONTH = "month"
    YEAR = "year"

class ChoiceId(str, Enum):
    PRESENT = "present"
    ABSENT = "absent"
    UNKNOWN = "unknown"

class TriageLevel(str, Enum):
    EMERGENCY_AMBULANCE = "emergency_ambulance"
    EMERGENCY = "emergency"
    CONSULTATION_24 = "consultation_24"
    CONSULTATION = "consultation"
    SELF_CARE = "self_care"