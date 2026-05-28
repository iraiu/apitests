import requests

from services.general.helpers.base_helper import BaseHelper


class TeacherHelper(BaseHelper):
    TEACHERS_ENDPOINT = "/teachers/"

    def post_teacher(self, json: dict) -> requests.Response:
        return self.api_utils.post(
            self.TEACHERS_ENDPOINT,
            json=json
        )
