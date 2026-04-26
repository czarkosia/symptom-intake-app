import uuid
from typing import List

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID, String, JSON, Integer, Boolean
from db.database import Base

from infermedica.enums import Sex, AgeUnit
from infermedica.models import EvidenceItem


class InterviewSession(Base):
    __tablename__ = 'interview_sessions'

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    age_value: Mapped[int] = mapped_column(Integer, nullable=False)
    age_unit: Mapped[AgeUnit] = mapped_column(String, nullable=False)
    sex: Mapped[Sex] = mapped_column(String, nullable=False)
    triage_level: Mapped[str] = mapped_column(String, nullable=True)
    evidence: Mapped[List[EvidenceItem]] = mapped_column(JSON, nullable=False, default=[])
    questions_asked: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_completed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

