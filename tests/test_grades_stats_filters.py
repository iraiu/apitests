from services.university.models.grade_stats_response import GradeStatsResponse


def get_expected_stats(grade_1: int, grade_2: int) -> GradeStatsResponse:
    grades = [grade_1, grade_2]

    return GradeStatsResponse(
        count=len(grades),
        min=min(grades),
        max=max(grades),
        avg=sum(grades) / len(grades)
    )


class TestGradesStatsFilters:

    def test_grades_stats_filtered_by_teacher(
            self,
            grades_stats_dataset
    ):
        university_service = grades_stats_dataset["university_service"]
        teacher = grades_stats_dataset["teacher"]
        grade_1 = grades_stats_dataset["grade_1"]
        grade_2 = grades_stats_dataset["grade_2"]

        response = university_service.get_grades_stats_raw(
            teacher_id=teacher.id
        )

        actual = GradeStatsResponse(**response.json())
        expected = get_expected_stats(grade_1, grade_2)

        assert actual == expected, (
            f"Expected {expected}, got {actual}. "
            f"Response: {response.text}"
        )

    def test_grades_stats_without_data_by_student(
            self,
            grades_stats_dataset
    ):
        university_service = grades_stats_dataset["university_service"]
        another_student = grades_stats_dataset["another_student"]
        teacher = grades_stats_dataset["teacher"]

        response = university_service.get_grades_stats_raw(
            student_id=another_student.id,
            teacher_id=teacher.id
        )

        actual = GradeStatsResponse(**response.json())

        expected = GradeStatsResponse(
            count=0,
            min=None,
            max=None,
            avg=None
        )

        assert actual == expected, (
            f"Expected {expected}, got {actual}. "
            f"Response: {response.text}"
        )