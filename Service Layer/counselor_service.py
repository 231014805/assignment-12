class CounselorService:
    def __init__(self, counselor_repo):
        self.counselor_repo = counselor_repo

    def update_availability(self, counselor_id, slot_id, status):
        slot = self.counselor_repo.find_slot_by_id(slot_id)
        if slot["counselor_id"] != counselor_id:
            raise ValueError("Invalid counselor slot")
        slot["isBooked"] = status
        return self.counselor_repo.update_slot(slot)
