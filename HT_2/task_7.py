'''Write a script to concatenate all elements 
in a list into a string and print it. List must 
include both strings and integers and must be hardcoded.'''

#my_list_elements = [43, 'List', 67, True]

def list_in_str(list_elements):
    result = " ".join(str(element) for element in list_elements)
    return result

#print(list_in_str(my_list_elements))