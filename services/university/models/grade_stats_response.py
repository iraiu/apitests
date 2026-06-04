from pydantic import BaseModel, ConfigDict, Field


class GradeStatsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int = Field(ge=0)
    min: int | None = Field(default=None, ge=0, le=5)
    max: int | None = Field(default=None, ge=0, le=5)
    avg: float | None = Field(default=None, ge=0, le=5)