from fastapi import FastAPI, HTTPException

app = FastAPI()

# Mock Repositories
student_repo = MockStudentRepository()
appointment_repo = MockAppointmentRepository()

# Services
student_service = StudentService(student_repo)
appointment_service = AppointmentService(appointment_repo)


@app.post("/students/register/")
async def register_student(name: str, email: str, phone: str, status: str):
    return student_service.register_student(name, email, phone, status)


@app.post("/appointments/schedule/")
async def schedule_appointment(student_id: int, counselor_id: int, date: str, time: str):
    try:
        return appointment_service.schedule_appointment(student_id, counselor_id, date, time)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
