from pydantic import BaseModel, ConfigDict, Field

MIN_GRADE = 0
MAX_GRADE = 5

class GradeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int = Field(gt=0)
    student_id: int = Field(gt=0)
    grade: int = Field(ge=MIN_GRADE, le=MAX_GRADE)