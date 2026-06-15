from services.university.models.grade_stats_response import GradeStatsResponse
from services.university.university_service import UniversityService


class TestGradesStatsContract:

    def test_get_grades_stats_success(
            self,
            university_api_utils_admin
    ):
        university_service = UniversityService(
            api_utils=university_api_utils_admin
        )

        response = university_service.get_grades_stats_raw()

        actual = response.status_code
        expected = 200

        assert actual == expected, (
            f"Expected status code {expected}, "
            f"got {actual}. "
            f"Response: {response.text}"
        )

    def test_get_grades_stats_without_auth(
            self,
            university_api_utils_anonym
    ):
        university_service = UniversityService(
            api_utils=university_api_utils_anonym
        )

        response = university_service.get_grades_stats_raw()

        actual = response.status_code
        expected = 403

        assert actual == expected, (
            f"Expected status code {expected}, "
            f"got {actual}. "
            f"Response: {response.text}"
        )

    def test_get_grades_stats_response_matches_schema(
            self,
            university_api_utils_admin
    ):
        university_service = UniversityService(
            api_utils=university_api_utils_admin
        )

        response = university_service.get_grades_stats_raw()

        GradeStatsResponse(**response.json())

    def test_get_grades_stats_min_not_greater_than_max(
            self,
            university_api_utils_admin
    ):
        university_service = UniversityService(
            api_utils=university_api_utils_admin
        )

        response = university_service.get_grades_stats_raw()
        stats = GradeStatsResponse(**response.json())

        actual = (
            stats.min is None
            or stats.max is None
            or stats.min <= stats.max
        )

        assert actual, (
            f"Expected min <= max or both nullable, "
            f"got min={stats.min}, max={stats.max}"
        )