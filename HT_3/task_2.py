'''Write a script to remove empty elements from a list.
    Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]'''

test_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]


print(f'List : {test_list}')
new_list = []
for i in test_list:
	if i:
		new_list.append(i)
print(f'New list : {new_list}')
