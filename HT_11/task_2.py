'''
Створити клас Person, в якому буде присутнім метод __init__ який буде приймати якісь аргументи,
які зберігатиме в відповідні змінні.
- Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
- Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атрибут profession
(його не має інсувати під час ініціалізації в самому класі) та виведіть його на екран (прінтоніть)
'''


class Person:

	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def show_age(self):
		return self.age

	def print_name(self):
		print(f"My name is {self.first_name} {self.last_name}.")

	def show_all_information(self):
		return f"My name is {self.first_name} {self.last_name}. I am {self.age} years old."


person_1 = Person("Tom", "Jonson", 34)
print(person_1.show_age())
person_1.print_name()
print(person_1.show_all_information())

person_2 = Person("Kate", "Lii", 27)
print(person_2.show_age())
person_2.print_name()
print(person_2.show_all_information())

person_1.profession = "Doctor"
print(person_1.profession)

person_2.profession = "Lawyer"
print(person_2.profession)
