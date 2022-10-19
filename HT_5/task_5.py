'''Написати функцію <fibonacci>, яка приймає один аргумент і виводить 
всі числа Фібоначчі, що не перевищують його.'''

def fibonacci(number):
	f_0 = 0
	f_1 = 1
	fibonacci_num = []
	fibonacci_num.append(f_0)
	while f_1 < number:
		fibonacci_num.append(f_1)
		f_2 = f_0 + f_1
		f_0 = f_1
		f_1 = f_2
	print(fibonacci_num)
	return fibonacci_num

#print(fibonacci(50))
