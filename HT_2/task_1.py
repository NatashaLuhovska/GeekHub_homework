'''Write a script which accepts a sequence of comma-separated numbers 
from user and generates a list and a tuple with those numbers.'''

float_map = map(float, input().split(","))

float_list = list(float_map)
float_tuple = tuple(float_list)

#print(float_list, float_tuple)
