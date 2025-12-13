# Definiujemy klasę Student (czyli szablon na studenta)
class Student:
    # Metoda __init__ uruchamia się w momencie tworzenia obiektu
    # self  -> konkretny student
    # name  -> imię studenta
    # marks -> lista ocen studenta
    def __init__(self, name, marks):
        self.name = name  # zapisujemy imię do obiektu
        self.marks = marks  # zapisujemy listę ocen do obiektu

    # Metoda sprawdzająca, czy student zdał
    def is_passed(self):
        # liczymy średnią ocen
        average = sum(self.marks) / len(self.marks)

        # zwracamy True jeśli średnia > 50, w przeciwnym razie False
        return average > 50


# ===== TWORZENIE OBIEKTÓW =====

# Student, który ZDA (średnia > 50)
student1 = Student("Anna", [60, 70, 80])

# Student, który NIE ZDA (średnia <= 50)
student2 = Student("Bartek", [30, 40, 50])


# ===== SPRAWDZENIE =====
print(student1.name, student1.is_passed())  # True
print(student2.name, student2.is_passed())  # False
