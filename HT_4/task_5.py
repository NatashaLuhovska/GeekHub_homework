'''Ну і традиційно - калькулятор :легкая_улыбка: Повинна бути 1 функцiя, 
яка приймає 3 аргументи - один з яких операцiя, яку зробити! Аргументи 
брати від юзера (можна по одному - окремо 2, окремо +, окремо 2; можна 
всі разом - типу 2 + 2). Операції що мають бути присутні: +, -, *, /, %, //, **. 
Не забудьте протестувати з різними значеннями на предмет помилок!'''

expr_input = input("Введіть вираз розділяючи значення та оператор пробілом:\n")

def calc(expresions):
	operations = ['+', '-', '*', '/', '%', '//', '**']
	exp_list = expresions.split(' ')

	try:
		if exp_list[1] == '+':
			return float(exp_list[0]) + float(exp_list[2])
		elif exp_list[1] == '-':
			return float(exp_list[0]) - float(exp_list[2])
		elif exp_list[1] == '*':
			return float(exp_list[0]) * float(exp_list[2])
		elif exp_list[1] == '/':
			return float(exp_list[0]) / float(exp_list[2])
		elif exp_list[1] == '%':
			return float(exp_list[0]) % float(exp_list[2])
		elif exp_list[1] == '//':
			return float(exp_list[0]) // float(exp_list[2])
		elif exp_list[1] == '**':
			return float(exp_list[0]) ** float(exp_list[2])
	except ZeroDivisionError:
		print("На нуль ділити не можна! Змініть значення чи оператор")
		return False
	except ValueError:
		print("Ви помилилися при введенні даних! Перевірте ваші значення та оператор.")
		print("Наш калькулятор працює тільки з дійсними числами та з такими операторами: +, -, *, /, %, //, **")
		return False

print(calc(expr_input))


