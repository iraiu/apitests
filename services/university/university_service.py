import requests

from services.general.base_service import BaseService
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.grade_helper import GradeHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.group_request import GroupRequest
from services.university.models.group_response import GroupResponse
from services.university.models.student_request import StudentRequest
from services.university.models.student_response import StudentResponse
from services.university.models.grade_request import GradeRequest
from services.university.models.grade_stats_response import GradeStatsResponse
from services.university.models.teacher_request import TeacherRequest
from utils.api_utils import ApiUtils
import os


class UniversityService(BaseService):
    SERVICE_URL = os.getenv ("UNIVERSITY_SERVICE_API_URL",
                             "http://localhost:8001")

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)
        self.grade_helper = GradeHelper(self.api_utils)
        self.teacher_helper = TeacherHelper(self.api_utils)

    def create_group(
            self,
            group_request: GroupRequest
    ) -> GroupResponse:
        response = self.group_helper.post_group(
            json=group_request.model_dump()
        )
        return GroupResponse(**response.json())

    def create_student(
            self,
            student_request: StudentRequest
    ) -> StudentResponse:
        response = self.student_helper.post_student(
            json=student_request.model_dump()
        )
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
        return self.grade_helper.get_grades_stats(
            student_id=student_id,
            teacher_id=teacher_id,
            group_id=group_id
        )

    def get_grades_stats(
            self,
            student_id: int | None = None,
            teacher_id: int | None = None,
            group_id: int | None = None
    ) -> GradeStatsResponse:
        response = self.get_grades_stats_raw(
            student_id=student_id,
            teacher_id=teacher_id,
            group_id=group_id
        )

        return GradeStatsResponse(**response.json())

    def create_grade(
            self,
            grade_request: GradeRequest
    ) -> requests.Response:
        return self.grade_helper.post_grade(
            data=grade_request.model_dump()
        )

    def create_teacher(
            self,
            teacher_request: TeacherRequest
    ) -> requests.Response:
        return self.teacher_helper.post_teacher(
            json=teacher_request.model_dump()
        )