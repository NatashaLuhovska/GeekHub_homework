'''Створіть клас в якому буде атрибут який буде рахувати кількість 
створених екземплярів класів.'''


class Student():
	count = 0

	def __init__(self, first_name):
		self.first_name = first_name
		Student.count += 1


p1 = Student("Tom")
print(p1.first_name)
print(p1.count)

p2 = Student("Mary")
print(p2.first_name)
print(p1.count)
print(p2.count)

p3 = Student("Nick")
print(p3.first_name)
print(p1.count)
print(p2.count)
print(p3.count)
