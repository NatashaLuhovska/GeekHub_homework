'''Write a script to remove values duplicates from 
dictionary. Feel free to hardcode your dictionary.'''

dict_1 = {'foo': 'bar', 'bar': 19, 'dou': 'bar', 'USD': 36, 'AUD': 19, 'name': 'Tom'}

print(f"Dictionary with dublicate values: {dict_1}")

new_dict = {}
unique_values = []
for key, value in dict_1.items():
	if value not in unique_values:
		unique_values.append(value)
		new_dict[key] = value

print(f"Dictionary without dublicate values: {new_dict}")