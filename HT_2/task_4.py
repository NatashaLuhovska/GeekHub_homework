'''Write a script which accepts a <number> from user and 
then <number> times asks user for string input. At the 
end script must print out result of concatenating all <number> strings.'''
number = int(input("Write a number: "))
result =''
for i in range(number):
    result += input("Write new str: ")
print(result)