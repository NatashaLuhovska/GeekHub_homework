"""1. Write a script that will run through a list of 
tuples and replace the last value for each tuple. The 
list of tuples can be hardcoded. The "replacement" value 
is entered by user. The number of elements in the tuples must 
be different."""


def reaplace_value_in_tuple(first_tuple, value):
	if len(first_tuple) == 0:
		print("Ви передали порожній tuple, виконати заміну не можливо!")
		return None
	new_list = list(first_tuple)
	new_list[-1] = value
	return tuple(new_list)

list_of_tupels = [(3,'SA',45),(34,'dfg','ert'),('3'),('a','s','d','f','g')]

print(f'List of tupels : {list_of_tupels}')

value = input("Write a new value: ")

result = []
for i in range(len(list_of_tupels)):
	result.append(reaplace_value_in_tuple(list_of_tupels[i], value))

print(f'New list with new value: {result}')


