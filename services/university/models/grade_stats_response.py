from pydantic import BaseModel, ConfigDict


class GradeStatsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int
    min: int | None
    max: int | None
    avg: float | None
