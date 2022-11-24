'''Створіть клас, який буде повністю копіювати поведінку list, за виключенням того, 
що індекси в ньому мають починатися з 1, а індекс 0 має викидати помилку (такого ж типу, 
яку кидає list якщо звернутися до неіснуючого індексу)'''

class MyList(list):
	def __init__(self, *my_list):
		self.my_list = list(my_list)

	def __getitem__(self, index):
		if index > 0:
			return self.my_list[index-1]
		elif index == 0:
			raise IndexError('list index out of range')
		else:
			return self.my_list[index]



k = MyList(3,4,7,8,5,7)
print(k[1])
print(k[4])
#print(k[0])
print(k[2:4])

	