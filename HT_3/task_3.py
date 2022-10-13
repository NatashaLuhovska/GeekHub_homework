'''Write a script to concatenate the following 
	dictionaries to create a NEW one.
    dict_1 = {'foo': 'bar', 'bar': 'buz'}
    dict_2 = {'dou': 'jones', 'USD': 36}
    dict_3 = {'AUD': 19.2, 'name': 'Tom'}'''

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}
new_dict = {}
new_dict.update(dict_1)
new_dict.update(dict_2)
new_dict.update(dict_3)
print(f'New dictionary: {new_dict}')
print(dict_1)