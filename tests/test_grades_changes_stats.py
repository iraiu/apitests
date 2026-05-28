from faker import Faker
from tests.factories.university_factory import UniversityFactory
from services.university.university_service import UniversityService

faker = Faker()


class TestGradesStatsHighLevel:

    def test_grades_stats_after_creating_grades(self,
                                                university_api_utils_admin):
        university_service = UniversityService(
            api_utils=university_api_utils_admin
        )
        factory = UniversityFactory(university_service)

        stats_before = university_service.get_grades_stats()

        teacher = factory.create_teacher()
        group = factory.create_group()
        student = factory.create_student(group_id=group.id)

        factory.create_grade(
            teacher_id=teacher.id,
            student_id=student.id,
            grade=4
        )

        factory.create_grade(
            teacher_id=teacher.id,
            student_id=student.id,
            grade=5
        )

        stats_after = university_service.get_grades_stats()

        assert stats_after.count == stats_before.count + 2
        assert stats_after.max >= 5
        assert stats_after.min <= 4
