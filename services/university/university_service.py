import requests
from services.general.base_service import BaseService
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.models.group_request import GroupRequest
from services.university.models.group_response import GroupResponse
from services.university.models.student_request import StudentRequest
from services.university.models.student_response import StudentResponse
from utils.api_utils import ApiUtils
from services.university.helpers.grade_helper import GradeHelper
from services.university.models.grade_request import GradeRequest
from services.university.models.grade_stats_response import GradeStatsResponse
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.teacher_request import TeacherRequest



class UniversityService(BaseService):
    SERVICE_URL = "http://localhost:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)
        self.grade_helper = GradeHelper(api_utils)
        self.grade_helper = GradeHelper(api_utils)
        self.teacher_helper = TeacherHelper(api_utils)

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(
            json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(self, student_request: StudentRequest) \
            -> StudentResponse:
        response = self.student_helper.post_student(
            json=student_request.model_dump())
        return StudentResponse(**response.json())

    def create_random_student(self):
        raise NotImplementedError

    def create_random_group_and_student(self):
        raise NotImplementedError

    def get_grades_stats_raw(
            self,
            student_id: int | None = None,
            teacher_id: int | None = None,
            group_id: int | None = None
    ) -> requests.Response:
        params = {
            "student_id": student_id,
            "teacher_id": teacher_id,
            "group_id": group_id,
        }
        params = {
            key: value
            for key, value in params.items()
            if value is not None
        }

        return self.grade_helper.get_grades_stats(
            params=params
        )

    def get_grades_stats(self) -> GradeStatsResponse:
        response = self.grade_helper.get_grades_stats()
        assert response.status_code == 200, response.text
        return GradeStatsResponse(**response.json())

    def create_grade(
            self,
            grade_request: GradeRequest
    ):
        return self.grade_helper.post_grade(
            data=grade_request.model_dump()
        )

    def create_teacher(
            self,
            teacher_request: TeacherRequest
    ):
        return self.teacher_helper.post_teacher(
            json=teacher_request.model_dump()
        )