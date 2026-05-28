import requests.status_codes

from services.university.helpers.group_helper import GroupHelper

from faker import Faker

faker = Faker()


class TestGroupContract:
    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.post_group({"name": faker.name()})

        assert (response.status_code ==
                requests.status_codes.codes.unauthorized), \
            (
                f"Wrong status code. Actual: '{response.status_code}',"
                f"" f"but expected: '{requests.status_codes.codes.unauthorized}'")
