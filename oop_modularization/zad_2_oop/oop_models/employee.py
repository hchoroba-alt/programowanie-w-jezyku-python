# ===== Employee =====
class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"Employee:\n"
            f"  Name: {self.first_name} {self.last_name}\n"
            f"  Hire date: {self.hire_date}\n"
            f"  Birth date: {self.birth_date}\n"
            f"  Address: {self.street}, {self.zip_code} {self.city}\n"
            f"  Phone: {self.phone}"
        )