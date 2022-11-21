'''Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки 
(включіть фантазію). Наприклад вона може містити класи Person, Teacher, Student, 
Book, Shelf, Author, Category і.т.д. Можна робити по прикладу банкомату з меню, 
базою даних і т.д.'''

import sqlite3


class Person:
	profession = ""

	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def take_a_book(self):
		print("Книги, доступні до видачі:")
		for row in cursor.execute('''SELECT * FROM books WHERE amount> 0 '''):
			print(row)
		id_book = int(input("Введіть номер обраної книги : "))
		if cursor.execute('''SELECT * FROM books WHERE book_id= ? ''', (id_book, )).fetchall():
			if self.profession == 'students':
				books = cursor.execute('''SELECT books FROM students WHERE first_name= ? AND last_name= ? ''',
										(self.first_name, self.last_name)).fetchall()[0][0]
				if books == None:
					cursor.execute('''UPDATE students SET books= ? WHERE first_name= ? AND last_name= ? ''',
									(str(id_book), self.first_name, self.last_name))
					conn.commit()
				else:
					cursor.execute('''UPDATE students SET books= ? WHERE first_name= ? AND last_name= ? ''',
									(books + ' '+str(id_book), self.first_name, self.last_name))
					conn.commit()
			elif self.profession == 'teachers':
				books = cursor.execute('''SELECT books FROM teachers WHERE first_name= ? AND last_name= ? ''',
										(self.first_name, self.last_name)).fetchall()[0][0]
				if books == None:
					cursor.execute('''UPDATE teachers SET books= ? WHERE first_name= ? AND last_name= ? ''',
									(str(id_book), self.first_name, self.last_name))
					conn.commit()
				else:
					cursor.execute('''UPDATE teachers SET books= ? WHERE first_name= ? AND last_name= ? ''',
									(books + ' '+str(id_book), self.first_name, self.last_name))
					conn.commit()
			amount_book = cursor.execute('''SELECT amount FROM books WHERE book_id= ? ''', (id_book, )).fetchall()[0][0]
			cursor.execute('''UPDATE books SET amount= ? WHERE book_id= ? ''', (amount_book-1, id_book))
			conn.commit()
			print(f"Дані внесені в Вашу картку!")
		else:
			print("Не коректно введені дані!")

	def list_books_in_person(self):
		if self.profession == 'students':
			books = cursor.execute('''SELECT books FROM students WHERE first_name= ? AND last_name= ? ''',
									(self.first_name, self.last_name)).fetchall()[0][0]
		elif self.profession == 'teachers':
			books = cursor.execute('''SELECT books FROM teachers WHERE first_name= ? AND last_name= ? ''',
									(self.first_name, self.last_name)).fetchall()[0][0]
		if books == None:
			return None
		for book_id in books.split(' '):
			print(cursor.execute('''SELECT * FROM books WHERE book_id= ? ''', (int(book_id), )).fetchall())
		return books.split(' ')

	def hand_in_the_book(self):
		print("Книги, доступні до видачі:")
		list_book_id = self.list_books_in_person()
		if list_book_id == None:
			print("Ви не маєте жодної книги на руках в даний момент. Можливо якась книга Вас цікавить?")
			return False
		id_book = input("Введіть номер обраної книги : ")
		if id_book in list_book_id:
			list_book_id.remove(id_book)
			if self.profession == 'students':
				cursor.execute('''UPDATE students SET books= ? WHERE first_name= ? AND last_name= ? ''',
								(' '.join(list_book_id), self.first_name, self.last_name))
				conn.commit()
			elif self.profession == 'teachers':
				cursor.execute('''UPDATE teachers SET books= ? WHERE first_name= ? AND last_name= ? ''',
								(' '.join(list_book_id), self.first_name, self.last_name))
				conn.commit()
			amount_book = cursor.execute('''SELECT amount FROM books WHERE book_id= ? ''', (int(id_book), )).fetchall()[0][0]
			cursor.execute('''UPDATE books SET amount= ? WHERE book_id= ? ''', (amount_book+1, int(id_book)))
			conn.commit()
			print(f"Дані внесені в Вашу картку!")
		else:
			print("Не коректно введені дані!")


class Student(Person):
	profession = "students"

	def __init__(self, first_name, last_name, age, group_name, course):
		super().__init__(first_name, last_name, age)
		self.group_name = group_name
		self.course = course


class Teacher(Person):
	profession = "teachers"

	def __init__(self, first_name, last_name, age, subject):
		super().__init__(first_name, last_name, age)
		self.subject = subject
		

class Librarian:

	def chek_user_in_Library(self):
		first_name = input("Введіть ім'я: ")
		last_name = input("Введіть прізвище: ")
		profession = input("Введіть професію(студент чи вчитель): ")
		if profession == 'студент':
			person = cursor.execute('''SELECT * FROM students WHERE first_name= ? AND last_name= ? ''', (first_name, last_name)).fetchall()
			if person:
				return Student(first_name, last_name, person[0][3], person[0][4], person[0][5])
		elif profession == 'вчитель':
			person = cursor.execute('''SELECT * FROM teachers WHERE first_name= ? AND last_name= ? ''', (first_name, last_name)).fetchall()
			if person:
				return Teacher(first_name, last_name, person[0][3], person[0][4])
		else:
			print("Не коректно введені дані!")
			return None

	def creat_new_user(self):
		profession = input("Введіть професію (студент чи вчитель): ")
		if profession == 'студент':
			first_name = input("Введіть ім'я:")
			last_name = input("Введіть прізвище: ")
			age = int(input("Введіть вік:"))
			group_name = input("Введіть спеціальність:")
			course = int(input("Введіть курс:"))
			id_student = len(cursor.execute("SELECT * FROM students").fetchall()) + 1
			cursor.execute('''
						INSERT INTO students (student_id, first_name, last_name, age, group_name, course, books)
						VALUES (?,?,?,?,?,?,?) ''', (id_student, first_name, last_name, age, group_name, course, None))
			conn.commit()
			return Student(first_name, last_name, age, group_name, course)
		elif profession == 'вчитель':
			first_name = input("Введіть ім'я:")
			last_name = input("Введіть прізвище: ")
			age = int(input("Введіть вік:"))
			subject = input("Введіть спеціальність:")
			id_teacher = len(cursor.execute("SELECT * FROM teachers").fetchall()) + 1
			cursor.execute('''
						INSERT INTO teachers (teacher_id, first_name, last_name, age, subject, books)
						VALUES (?,?,?,?,?,?) ''', (id_teacher, first_name, last_name, age, subject, None))
			conn.commit()
			return Teacher(first_name, last_name, age, subject)
		else:
			print("Не коректно введені дані!")


def start():
	librarian = Librarian()
	while True:
		print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n')
		print('{:^50}'.format("Вітаємо! \n"))
		print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n') 
		print("Яку дію бажаєте виконати? \n")
		print('*************************************************** \n') 
		operations = """            
		Увійти             --  Натисніть 1
		Зареєструватися    --  Натисніть 2
		Вийти              --  Натисніть 0
		"""
		print(operations)
		print('***************************************************') 
		operation = input()
		if operation == '1':
			user = librarian.chek_user_in_Library()
		elif operation == '2':
			user = librarian.creat_new_user()
		elif operation == '0':
			print('До зустрічі!')
			break
		else:
			print("Не правильно введене значення!")
		if user:
			break
	while user:
		print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& \n') 
		print("Яку дію бажаєте виконати?")
		print('********************************************************* \n') 
		operations = """            
		Взяти книгу             --  Натисніть 1
		Повернути книгу         --  Натисніть 2
		Вихід                   --  Натисніть 0 
		"""
		print(operations)
		print('********************************************************* ') 
		operation = input()
		if operation == '1':
			user.take_a_book()
		elif operation == '2':
			user.hand_in_the_book()
		elif operation == '0':
			print('До нових зустрічей!')
			break
		else:
			print("Не правильно введене значення!")
		print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& \n')


conn = sqlite3.connect('library_database.db') 
cursor = conn.cursor()
start()
conn.commit()
conn.close()