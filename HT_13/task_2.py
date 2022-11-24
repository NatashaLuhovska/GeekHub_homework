'''Створити клас Matrix, який буде мати наступний функціонал:
1. __init__ - вводиться кількість стовпців і кількість рядків
2. fill() - заповнить створений масив числами - по порядку. Наприклад:
+────+────+
| 1  | 2  |
+────+────+
| 3  | 4  |
+────+────+
| 5  | 6  |
+────+────+
3. print_out() - виведе створений масив (якщо він ще не заповнений даними - вивести нулі
4. transpose() - перевертає створений масив. Тобто, якщо взяти попередню таблицю, результат буде
+────+────+────+
| 1  | 3  | 5  |
+────+────+────+
| 2  | 4  | 6  |
+────+────+────+
P.S. Всякі там Пандас/Нампай не використовувати - тільки хардкор ;)
P.P.S. Вивід не обов’язково оформлювати у вигляді таблиці - головне, щоб було видно, що це окремі стовпці / рядки'''


class Matrix:
	def __init__(self, number_of_rows, number_of_columns):
		self.number_of_rows = number_of_rows
		self.number_of_columns = number_of_columns
		self.matrix = [[0 for j in range(number_of_columns)] for i in range(number_of_rows)]

	def fill(self):
		i = 1
		for row in range(self.number_of_rows):
			for column in range(self.number_of_columns):
				self.matrix[row][column] = i
				i += 1

	def print_out(self):
		for row in self.matrix:
			print(' ', '   '.join([str(k) for k in row]), end='\n')
			print()

	def transpose(self):
		t_matrix = [[0 for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
		for column in range(len(self.matrix[0])):
			for row in range(len(self.matrix)):
				t_matrix[column][row] = self.matrix[row][column]
		self.matrix = t_matrix

		
matrix_1 = Matrix(3, 2)
matrix_1.print_out()
matrix_1.fill()
matrix_1.print_out()
matrix_1.transpose()
matrix_1.print_out()
matrix_1.transpose()
matrix_1.print_out()
