'''Напишіть функцію,яка приймає рядок з декількох слів і повертає 
довжину найкоротшого слова. Реалізуйте обчислення за допомогою 
генератора в один рядок.'''

def len_short_word(string):
	return min([len(word) for word in string.split(' ')])

#string = "Dogs are wise"
#print(len_short_word(string))