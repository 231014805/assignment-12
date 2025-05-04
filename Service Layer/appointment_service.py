class AppointmentService:
    def __init__(self, appointment_repo):
        self.appointment_repo = appointment_repo

    def schedule_appointment(self, student_id, counselor_id, date, time):
        existing = self.appointment_repo.find_by_counselor_and_time(counselor_id, date, time)
        if existing:
            raise ValueError("Time slot already booked")
        appointment = {
            "student_id": student_id,
            "counselor_id": counselor_id,
            "date": date,
            "time": time,
            "status": "Scheduled"
        }
        return self.appointment_repo.save(appointment)

    def cancel_appointment(self, appointment_id):
        appointment = self.appointment_repo.find_by_id(appointment_id)
        if not appointment:
            raise ValueError("Appointment not found")
        appointment["status"] = "Canceled"
        return self.appointment_repo.update(appointment)
