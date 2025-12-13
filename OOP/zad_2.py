# ===== Student =====
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


# ===== Library =====
class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"Library:\n"
            f"  Address: {self.street}, {self.zip_code} {self.city}\n"
            f"  Open hours: {self.open_hours}\n"
            f"  Phone: {self.phone}"
        )


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
        phone: str
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


# ===== Book =====
class Book:
    def __init__(
        self,
        library: Library,
        public_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int
    ):
        self.library = library
        self.public_date = public_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return (
            f"Book:\n"
            f"  Author: {self.author_name} {self.author_surname}\n"
            f"  Published: {self.public_date}\n"
            f"  Pages: {self.number_of_pages}\n"
            f"  Library:\n{self.library}"
        )


# ===== Order =====
class Order:
    def __init__(
        self,
        employee: Employee,
        student: Student,
        books: list[Book],
        order_date: str
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        books_str = "\n".join(str(book) for book in self.books)
        return (
            f"Order:\n"
            f"  Date: {self.order_date}\n"
            f"\n"
            f"  Student:\n{self.student}\n"
            f"\n"
            f"  Employee:\n{self.employee}\n"
            f"\n"
            f"  Books:\n{books_str}"
        )


# ===== INSTANCJE =====
library1 = Library("Warszawa", "Marszałkowska 10", "00-001", "8:00-18:00", "111-222-333")
library2 = Library("Kraków", "Długa 5", "30-001", "9:00-17:00", "444-555-666")

book1 = Book(library1, "2010", "Adam", "Mickiewicz", 300)
book2 = Book(library1, "2015", "Henryk", "Sienkiewicz", 450)
book3 = Book(library2, "2020", "Olga", "Tokarczuk", 380)
book4 = Book(library2, "2005", "Bolesław", "Prus", 520)
book5 = Book(library1, "2018", "Andrzej", "Sapkowski", 600)

employee1 = Employee("Jan", "Kowalski", "2020-01-01", "1990-05-05", "Warszawa", "Polna 3", "00-100", "123-123-123")
employee2 = Employee("Anna", "Nowak", "2018-06-15", "1988-03-12", "Kraków", "Leśna 7", "30-200", "234-234-234")
employee3 = Employee("Piotr", "Zieliński", "2022-09-01", "1995-11-20", "Warszawa", "Słoneczna 9", "00-300", "345-345-345")

student1 = Student("Kasia", [60, 70, 80])
student2 = Student("Tomek", [30, 40, 50])
student3 = Student("Ola", [90, 85, 95])

order1 = Order(employee1, student1, [book1, book2], "2025-12-13")
order2 = Order(employee2, student3, [book3, book4, book5], "2025-12-14")

print(order1)
print("\n" + "=" * 40 + "\n")
print(order2)
