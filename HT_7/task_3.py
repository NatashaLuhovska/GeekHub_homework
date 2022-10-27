'''Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції. 
Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію 
   по ній: https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації (типу range(1, -10, 5) тощо). 
   Подивіться як веде себе стандартний range в таких випадках.'''

def my_range(*args):
	if len(args) == 1:
		start = 0
		stop = args[0]
		step = 1
	elif len(args) == 2:
		start = args[0]
		stop = args[1]
		step = 1
	elif len(args) == 3:
		start = args[0]
		stop = args[1]
		step = args[2]
	if step > 0 and start < stop:
		while start < stop:
			yield start
			start += step  
	elif step < 0 and start > stop:
		while start > stop:
			yield start
			start += step 
	else:
		print("Ви ввели некоректні дані!!!!")



#for i in my_range(0,-9,-2)
#	print(i)

