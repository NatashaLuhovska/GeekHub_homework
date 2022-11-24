'''Створіть клас Car, який буде мати властивість year (рік випуску). Додайте всі необхідні методи до класу,
 щоб можна було виконувати порівняння car1 > car2 , яке буде показувати, що car1 старша за car2. Також, 
 операція car1 - car2 повинна повернути різницю між роками випуску. '''

class Car:
    def __init__(self, year):
        self.year = year

    def __sub__(self, other):
        return abs(self.year - other.year)

    def __lt__(self, other):
        if self.year - other.year > 0:
            return True
        else:
            return False


car_1 = Car(2013)

car_2 = Car(2000)

print(car_1 - car_2)
print(car_1 > car_2)
print(car_1 < car_2)