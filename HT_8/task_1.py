'''1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів. Після запуска програми на екран виводиться 
   в лівій половині - колір автомобільного, а в правій - пішохідного світлофора. Кожну 1 секунду виводиться 
   поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних 
   світлофорах (пішоходам зелений тільки коли автомобілям червоний).
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green'''

import time


def lights_for_pedestrian(color_for_car):
	if color_for_car == "Red":
		return "Green"
	else:
		return "Red"


colors_dict = {"Red" : 4, "Yellow" : 2, "Green" : 4} 
colors_list = ["Red", "Yellow", "Green", "Yellow"]


while True:
	for i in colors_list:
		for j in range(colors_dict.get(i)):
			print(f'{i:50} {lights_for_pedestrian(i)}')
			time.sleep(1)

