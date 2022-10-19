'''Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона,
і вертатиме список простих чисел всередині цього діапазона. Не забудьте про перевірку на 
валідність введених даних та у випадку невідповідності - виведіть повідомлення.'''

def is_prime(number):
	for i in range(2, int(number ** 0.5)+1):
		if number % i == 0:
			return False
	return True

def prime_list(start : int, stop : int):
	if not isinstance(start, int) or not isinstance(stop, int):
		print("Початок і кінець діапазону мають бути натуральними числами!!!")
		return "Ви ввели некоректні дані!"
	list_of_prime = []
	for i in range(start + 1, stop):
		if is_prime(i):
			list_of_prime.append(i)
	return list_of_prime

print(prime_list(5.6, 220))

