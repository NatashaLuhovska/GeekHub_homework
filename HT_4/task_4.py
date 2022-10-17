'''Наприклад маємо рядок 
--> "f98neroi4nr0c3n30irn03ien3c0rfe kdno400we(nw,kowe%00koi!jn35pijnp4 6ij7k5j78p3kj546p4 65jnpoj35po6j345" 
-> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати довільні рядки на зразок цього та яка обробляє наступні випадки:
-  якщо довжина рядка в діапазоні 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всіх чисел та окремо рядок без цифр та знаків лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)'''

def sum_alpha_num(string):
	sum_num = 0
	alph_str = ''
	for i in string:
		if i.isdigit():
			sum_num += int(i)
		if i.isalpha():
			alph_str += i
	return (sum_num, alph_str)

def count_alpha_num(string):
	num = 0
	alph = 0
	for i in string:
		if i.isdigit():
			num += 1
		if i.isalpha():
			alph += 1
	return (num, alph)

def symbols(string):
	symb = ''
	for i in string:
		if not i.isdigit() and not i.isalpha():
			symb += i
	return symb

def text_processing(string):
	if len(string) < 30:
		new_str = sum_alpha_num(string)
		print(f'Cума цифр: {new_str[0]}')
		print(f'Рядок тільки з букв: \n{new_str[1]}')
	elif len(string) <= 50:
		count_str = count_alpha_num(string)
		print(f'Довжина рядка - {len(string)}, букв у рядку - {count_str[1]}, цифр у рядку - {count_str[0]}')
	else:
		print(f'Символи рядка: {symbols(string)}')

#string = "f98neroi4nr0c3nwe2wed%00"
#print(sum_alpha_num(string))
#print(count_alpha_num(string))
#print(symbols(string))
#text_processing(string)