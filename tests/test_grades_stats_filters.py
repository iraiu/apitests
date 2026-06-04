from services.university.models.grade_stats_response import GradeStatsResponse


class TestGradesStatsFilters:

    def test_grades_stats_filtered_by_student(
            self,
            grades_stats_dataset
    ):
        university_service = grades_stats_dataset["university_service"]
        student = grades_stats_dataset["student"]

        response = university_service.get_grades_stats_raw(
            student_id=student.id
        )

        actual = (
            response.status_code,
            GradeStatsResponse(**response.json())
            if response.status_code == 200
            else response.text
        )

        expected = (
            200,
            GradeStatsResponse(
                count=2,
                min=4,
                max=5,
                avg=4.5
            )
        )

        assert actual == expected, (
            f"Expected {expected}, got {actual}"
        )

    def test_grades_stats_filtered_by_teacher(
            self,
            grades_stats_dataset
    ):
        university_service = grades_stats_dataset["university_service"]
        teacher = grades_stats_dataset["teacher"]

        response = university_service.get_grades_stats_raw(
            teacher_id=teacher.id
        )

        actual = (
            response.status_code,
            GradeStatsResponse(**response.json())
            if response.status_code == 200
            else response.text
        )

        expected = (
            200,
            GradeStatsResponse(
                count=2,
                min=4,
                max=5,
                avg=4.5
            )
        )

        assert actual == expected, (
            f"Expected {expected}, got {actual}"
        )

    def test_grades_stats_filtered_by_group(
            self,
            grades_stats_dataset
    ):
        university_service = grades_stats_dataset["university_service"]
        group = grades_stats_dataset["group"]

        response = university_service.get_grades_stats_raw(
            group_id=group.id
        )

        actual = (
            response.status_code,
            GradeStatsResponse(**response.json())
            if response.status_code == 200
            else response.text
        )

        expected = (
            200,
            GradeStatsResponse(
                count=2,
                min=4,
                max=5,
                avg=4.5
            )
        )

        assert actual == expected, (
            f"Expected {expected}, got {actual}"
        )

    def test_grades_stats_filtered_by_student_and_teacher(
            self,
            grades_stats_dataset
    ):
        university_service = grades_stats_dataset["university_service"]
        student = grades_stats_dataset["student"]
        teacher = grades_stats_dataset["teacher"]

        response = university_service.get_grades_stats_raw(
            student_id=student.id,
            teacher_id=teacher.id
        )

        actual = (
            response.status_code,
            GradeStatsResponse(**response.json())
            if response.status_code == 200
            else response.text
        )

        expected = (
            200,
            GradeStatsResponse(
                count=2,
                min=4,
                max=5,
                avg=4.5
            )
        )

        assert actual == expected, (
            f"Expected {expected}, got {actual}"
        )

    def test_grades_stats_without_data_by_student(
            self,
            grades_stats_dataset
    ):
        university_service = grades_stats_dataset["university_service"]
        another_student = grades_stats_dataset["another_student"]

        response = university_service.get_grades_stats_raw(
            student_id=another_student.id,
            teacher_id=grades_stats_dataset["teacher"].id
        )

        actual = (
            response.status_code,
            GradeStatsResponse(**response.json())
            if response.status_code == 200
            else response.text
        )

        expected = (
            200,
            GradeStatsResponse(
                count=0,
                min=None,
                max=None,
                avg=None
            )
        )

        assert actual == expected, (
            f"Expected {expected}, got {actual}"
        )