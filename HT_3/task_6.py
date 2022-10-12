'''Write a script to get the maximum and 
minimum VALUE in a dictionary.'''

dict_1 = {'foo': 'bar', 'bar': 19, 'dou': 'bar', 'USD': 36, 'AUD': 19, 'name': 'Tom'}

print(f"Dictionary with dublicate values: {dict_1}")

new_dict = {}


new_dict = {}
unique_values = []
for key, value in dict_1.items():
	if type(value) == int or type(value) == float:
		new_dict[key] = value

max_value = max(new_dict.values())
min_value = min(new_dict.values())



print(f'Maximum value : {max_value}')
print(f'Minimum value : {min_value}')