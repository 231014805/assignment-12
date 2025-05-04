class MockStudentRepository:
    def __init__(self):
        self.students = []

    def save(self, student):
        self.students.append(student)
        return student

    def find_by_email(self, email):
        return next((s for s in self.students if s["email"] == email), None)


class MockAppointmentRepository:
    def __init__(self):
        self.appointments = []

    def save(self, appointment):
        self.appointments.append(appointment)
        return appointment

    def find_by_id(self, appointment_id):
        return next((a for a in self.appointments if a["id"] == appointment_id), None)
