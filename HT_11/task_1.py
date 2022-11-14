'''
Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні
виконувати математичні операції з 2-ма числами, а саме додавання, віднімання,
множення, ділення.
- Якщо під час створення екземпляру класу звернутися до атрибута last_result
він повинен повернути пусте значення.
- Якщо використати один з методів - last_result повинен повернути результат
виконання ПОПЕРЕДНЬОГО методу.
    Example:
    last_result --> None
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6
    ...
- Додати документування в клас (можете почитати цю статтю:
https://realpython.com/documenting-python-code/ )

'''


class Calc:
	'''
	A class used to perform mathematical operations

	Attributes
	----------
	last_result : int or float
		the previous result of the method call (default None)
	result : int or float
		the result of the method call (default None)
	'''

	last_result = None
	result = None

	def addition(self, num_1, num_2):
		'''
		Adding two elements.

		Parameters
		----------
		num_1 : int or float
			First element
		num_2 : int or float
			Second element
		'''

		self.last_result = self.result
		self.result = num_1 + num_2

	def subtraction(self, num_1, num_2):
		'''
		Subtracting two elements.

		Parameters
		----------
		num_1 : int or float
			First element
		num_2 : int or float
			Second element
		'''

		self.last_result = self.result
		self.result = num_1 - num_2

	def multiplication(self, num_1, num_2):
		'''
		Multiplicating two elements.

		Parameters
		----------
		num_1 : int or float
			First element
		num_2 : int or float
			Second element
		'''

		self.last_result = self.result
		self.result = num_1 * num_2

	def division(self, num_1, num_2):
		'''
		Division of two elements.

		Parameters
		----------
		num_1 : int or float
			First element
		num_2 : int or float
			Second element
		'''

		self.last_result = self.result
		self.result = num_1 / num_2


calculus = Calc()

calculus.addition(6, 8)
print(calculus.last_result)

calculus.subtraction(6, 8)
print(calculus.last_result)

calculus.multiplication(6, 8)
print(calculus.last_result)

calculus.division(64, 8)
print(calculus.last_result)

calculus.addition(6, 8)
print(calculus.last_result)
