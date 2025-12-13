# ===== Order =====
class Order:
    def __init__(
        self, employee: Employee, student: Student, books: list[Book], order_date: str
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