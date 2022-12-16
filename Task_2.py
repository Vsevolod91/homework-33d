from Task_1 import Item

class Phone(Item):
    def __init__(self, name, price, quantity, broken_phones):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

phone1 = Phone("iPhone 10", 500, 5, 1)

print(phone1)