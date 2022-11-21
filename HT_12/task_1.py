'''Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color з 
початковим значенням white і метод для зміни кольору фігури, а його підкласи «овал» (Oval) 
і «квадрат» (Square) містять методи _init_ для завдання початкових розмірів об'єктів при 
їх створенні.'''

class Figure:
	color = 'white'

	def change_color(self, new_color):
		self.color = new_color


class Oval(Figure):

	def __init__(self, a, b):
		self.a = a
		self.b = b


class Square(Figure):

	def __init__(self, a):
		self.a = a


elips_1 = Oval(3, 5)
print(elips_1.color)
elips_1.change_color("green")
print(elips_1.color)

square_1 = Square(7)
print(square_1.color)
square_1.change_color("red")
print(square_1.color)
