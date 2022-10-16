'''Створіть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна 
повертати якийсь результат (напр. інпут від юзера, результат математичної 
операції тощо). Також створiть четверту ф-цiю, яка всередині викликає 3 попередні,
обробляє їх результат та також повертає результат своєї роботи. Таким чином ми будемо 
викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.'''

def say_hello():
	name = input("Як до вас звертатися? \n")
	print(f"Вітаємо, {name}!")
	return name

def average_marks(marks):
	return round(sum(marks)/len(marks), 2)

def in_rating():
	marks = input("Ввведіть оцінки, які ви отримали на сесії, через пробіл: \n").split(' ')
	marks_list = list(map(float, marks))
	if 2 in marks_list:
		print("Ви втратили право на стипендію!")
	elif len(marks_list) < 10:
		print("Сесія ще не завершена для вас!")
	elif average_marks(marks_list)>=4:
		print("Ви в рейтингу на стипендію! Очікуйте результатів.")
	return marks_list

def student_info():
	student = {}
	student['Name'] = say_hello()
	student['Marks'] = in_rating()
	student['Average marks'] = average_marks(student['Marks'])
	return student
	

print(student_info())
