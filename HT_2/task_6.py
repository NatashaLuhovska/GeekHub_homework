'''Write a script to check whether a value from user input is 
contained in a group of values.
e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
     [1, 2, 'u', 'a', 4, True] --> 5 --> False'''

group = map(str,input("Write a group :").split(","))
element = input("Write an element: ")

print(element in group)



