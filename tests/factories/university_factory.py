import random

from faker import Faker

from services.university.models.grade_request import GradeRequest
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.models.base_student import DegreeEnum

faker = Faker()


class UniversityFactory:

    @staticmethod
    def teacher_request(subject: str = "History") -> TeacherRequest:
        return TeacherRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            subject=subject
        )

    @staticmethod
    def group_request() -> GroupRequest:
        return GroupRequest(
            name=faker.name()
        )

    @staticmethod
    def student_request(group_id: int) -> StudentRequest:
        return StudentRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            degree=random.choice([option for option in DegreeEnum]),
            phone=faker.numerify("+7##########"),
            group_id=group_id
        )

    @staticmethod
    def grade_request(
            teacher_id: int,
            student_id: int,
            grade: int
    ) -> GradeRequest:
        return GradeRequest(
            teacher_id=teacher_id,
            student_id=student_id,
            grade=grade
        )