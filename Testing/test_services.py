import pytest

from student_service import StudentService
from mock_repositories import MockStudentRepository


def test_register_student():
    repo = MockStudentRepository()
    service = StudentService(repo)
    result = service.register_student("John Doe", "john@example.com", "1234567890", "Active")
    assert result["name"] == "John Doe"
    assert len(repo.students) == 1
