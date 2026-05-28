import random

from faker import Faker

from services.university.models.grade_request import GradeRequest
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.models.base_student import DegreeEnum

faker = Faker()


class UniversityFactory:

    def __init__(self, university_service):
        self.university_service = university_service

    def create_teacher(self):
        return self.university_service.create_teacher(
            teacher_request=TeacherRequest(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                subject="History"
            )
        )

    def create_group(self):
        return self.university_service.create_group(
            group_request=GroupRequest(
                name=faker.name()
            )
        )

    def create_student(self, group_id: int):
        return self.university_service.create_student(
            student_request=StudentRequest(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                degree=random.choice([option for option in DegreeEnum]),
                phone=faker.numerify("+7##########"),
                group_id=group_id
            )
        )

    def create_grade(self, teacher_id: int, student_id: int, grade: int):
        return self.university_service.create_grade(
            grade_request=GradeRequest(
                teacher_id=teacher_id,
                student_id=student_id,
                grade=grade
            )
        )
