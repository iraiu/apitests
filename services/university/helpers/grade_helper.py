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

    def get_grades_stats(self) -> requests.Response:
        return self.api_utils.get(
            self.GRADES_STATS_ENDPOINT
        )
