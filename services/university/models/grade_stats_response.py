from pydantic import BaseModel, ConfigDict, Field

from services.university.models.grade_request import (
    MIN_GRADE,
    MAX_GRADE
)


class GradeStatsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int = Field(ge=0)
    min: int | None = Field(
        default=None,
        ge=MIN_GRADE,
        le=MAX_GRADE
    )
    max: int | None = Field(
        default=None,
        ge=MIN_GRADE,
        le=MAX_GRADE
    )
    avg: float | None = Field(
        default=None,
        ge=MIN_GRADE,
        le=MAX_GRADE
    )