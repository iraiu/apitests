import requests

from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    GRADES_ENDPOINT = "/grades/"
    GRADES_STATS_ENDPOINT = "/grades/stats/"

    def post_grade(self, data: dict) -> requests.Response:
        return self.api_utils.post(
            self.GRADES_ENDPOINT,
            data=data
        )

    def get_grades_stats(
            self,
            student_id: int | None = None,
            teacher_id: int | None = None,
            group_id: int | None = None
    ) -> requests.Response:
        params = {
            "student_id": student_id,
            "teacher_id": teacher_id,
            "group_id": group_id
        }

        params = {
            key: value
            for key, value in params.items()
            if value is not None
        }

        return self.api_utils.get(
            self.GRADES_STATS_ENDPOINT,
            params=params
        )