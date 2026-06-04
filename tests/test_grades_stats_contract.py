from services.university.university_service import UniversityService


class TestGradesStatsContract:

    def test_get_grades_stats_success(self, university_api_utils_admin):
        university_service = UniversityService(
            api_utils=university_api_utils_admin
        )

        response = university_service.get_grades_stats_raw()

        assert response.status_code == 200, response.text

    def test_get_grades_stats_without_auth(self, university_api_utils_anonym):
        university_service = UniversityService(
            api_utils=university_api_utils_anonym
        )

        response = university_service.get_grades_stats_raw()

        assert response.status_code == 403, (
            f"Expected status code 403, "
            f"got {response.status_code}. "
            f"Response: {response.text}"
        )

    def test_get_grades_stats_schema(self, university_api_utils_admin):
        university_service = UniversityService(
            api_utils=university_api_utils_admin
        )

        stats = university_service.get_grades_stats()

        assert stats.count >= 0

        if stats.min is not None and stats.max is not None:
            assert stats.min <= stats.max
