import pytest
from faker import Faker

from logger.logger import Logger
from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.models.grade_request import MAX_GRADE
from services.university.models.grade_response import GradeResponse
from services.university.models.teacher_response import TeacherResponse
from services.university.university_service import UniversityService
from tests.factories.university_factory import UniversityFactory
from utils.api_utils import ApiUtils


faker = Faker()


@pytest.fixture(scope="session", autouse=True)
def setup_logger():
    Logger.init()


@pytest.fixture(scope="function")
def auth_api_utils_anonym():
    return ApiUtils(url=AuthService.SERVICE_URL)


@pytest.fixture(scope="function")
def university_api_utils_anonym():
    return ApiUtils(url=UniversityService.SERVICE_URL)


@pytest.fixture(scope="function")
def access_token(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)

    username = f"{faker.user_name()}_{faker.uuid4()}"
    password = faker.password(
        length=30,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )

    auth_service.register_user(
        register_request=RegisterRequest(
            username=username,
            password=password,
            password_repeat=password,
            email=faker.email()
        )
    )

    login_response = auth_service.login_user(
        login_request=LoginRequest(
            username=username,
            password=password
        )
    )

    return login_response.access_token


@pytest.fixture(scope="function")
def auth_api_utils_admin(access_token):
    return ApiUtils(
        url=AuthService.SERVICE_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )


@pytest.fixture(scope="function")
def university_api_utils_admin(access_token):
    return ApiUtils(
        url=UniversityService.SERVICE_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )


@pytest.fixture(scope="function")
def grades_stats_dataset(university_api_utils_admin):
    university_service = UniversityService(
        api_utils=university_api_utils_admin
    )

    teacher_response = university_service.create_teacher(
        teacher_request=UniversityFactory.create_teacher_request()
    )
    teacher = TeacherResponse(**teacher_response.json())

    another_teacher_response = university_service.create_teacher(
        teacher_request=UniversityFactory.create_teacher_request()
    )
    another_teacher = TeacherResponse(**another_teacher_response.json())

    group = university_service.create_group(
        group_request=UniversityFactory.create_group_request()
    )

    another_group = university_service.create_group(
        group_request=UniversityFactory.create_group_request()
    )

    student = university_service.create_student(
        student_request=UniversityFactory.create_student_request(
            group_id=group.id
        )
    )

    another_student = university_service.create_student(
        student_request=UniversityFactory.create_student_request(
            group_id=another_group.id
        )
    )

    grade_1 = MAX_GRADE - 1
    grade_2 = MAX_GRADE
    another_grade = MAX_GRADE - 4

    grade_response_1 = university_service.create_grade(
        grade_request=UniversityFactory.create_grade_request(
            teacher_id=teacher.id,
            student_id=student.id,
            grade=grade_1
        )
    )
    GradeResponse(**grade_response_1.json())

    grade_response_2 = university_service.create_grade(
        grade_request=UniversityFactory.create_grade_request(
            teacher_id=teacher.id,
            student_id=student.id,
            grade=grade_2
        )
    )
    GradeResponse(**grade_response_2.json())

    another_grade_response = university_service.create_grade(
        grade_request=UniversityFactory.create_grade_request(
            teacher_id=another_teacher.id,
            student_id=another_student.id,
            grade=another_grade
        )
    )
    GradeResponse(**another_grade_response.json())

    return {
        "university_service": university_service,
        "teacher": teacher,
        "student": student,
        "group": group,
        "another_student": another_student,
        "grade_1": grade_1,
        "grade_2": grade_2,
    }