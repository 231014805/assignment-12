class StudentService:
    def __init__(self, student_repo):
        self.student_repo = student_repo

    def register_student(self, name, email, phone, status):
        student = {
            "name": name,
            "email": email,
            "phone": phone,
            "status": status,
        }
        return self.student_repo.save(student)

    def login(self, email, password):
        student = self.student_repo.find_by_email(email)
        if not student or student.get("password") != password:
            raise ValueError("Invalid credentials")
        return student

    def book_appointment(self, student_id, appointment_id):
        appointment = self.student_repo.find_appointment_by_id(appointment_id)
        if appointment.get("status") != "Available":
            raise ValueError("Appointment is not available")
        appointment["status"] = "Booked"
        appointment["student_id"] = student_id
        return self.student_repo.update_appointment(appointment)
