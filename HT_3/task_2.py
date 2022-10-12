'''Write a script to remove empty elements from a list.
    Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]'''

test_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]


print(f'List : {test_list}')
new_list = []
for i in test_list:
	if bool(i) == True:
		new_list.append(i)
print('New list : {new_list}')
