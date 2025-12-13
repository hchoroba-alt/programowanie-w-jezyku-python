# ===== Book =====
class Book:
    def __init__(
        self,
        library: Library,
        public_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
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