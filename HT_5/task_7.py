'''Написати функцію, яка приймає на вхід список (через кому), підраховує 
кількість однакових елементів у ньому і виводить результат. Елементами 
списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> 
    "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"'''

def count_same_elements(list_of_elem):
	unique_values = []
	unique = []
	new = []
	for i in list_of_elem:
		if i not in unique:
			unique.append(i)
	for i in list_of_elem:
		for j in unique:
			if i == j and type(i) != type(j):
				new.append(i)
	unique += new
	
	for key in unique:
		k = 0
		for elem in list_of_elem:
			if key == elem and type(key) == type(elem):
				k += 1
		unique_values.append((str(key), str(k)))

	return  ', '.join([' -> '.join(i) for i in unique_values])


my_list =[1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]

print(count_same_elements(my_list))