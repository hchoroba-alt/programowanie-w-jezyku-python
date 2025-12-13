class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = int(price)
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"House:\n"
            f"  Area: {self.area} m2\n"
            f"  Rooms: {self.rooms}\n"
            f"  Price: {self.price}\n"
            f"  Address: {self.address}\n"
            f"  Plot size: {self.plot} m2"
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Flat:\n"
            f"  Area: {self.area} m2\n"
            f"  Rooms: {self.rooms}\n"
            f"  Price: {self.price}\n"
            f"  Address: {self.address}\n"
            f"  Floor: {self.floor}"
        )


house = House(120, 5, 850000, "Warszawa, ul. Leśna 3", 600)
flat = Flat(55, 2, 420000, "Kraków, ul. Długa 12", 3)

print(house)
print(flat)
