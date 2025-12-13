# ==============================
# ZADANIE 2 — student.py
# ==============================
# Ten plik zawiera tylko klasę Student.

class Student:
    def __init__(self, name: str, marks: list[int]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        average = sum(self.marks) / len(self.marks)
        return average > 50

    def __str__(self) -> str:
        status = "PASSED" if self.is_passed() else "FAILED"
        return (
            f"Student:\n"
            f"  Name: {self.name}\n"
            f"  Marks: {self.marks}\n"
            f"  Status: {status}"
        )
