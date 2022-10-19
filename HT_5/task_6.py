'''Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів 
в списку. Тобто функція приймає два аргументи: список і величину зсуву 
(якщо ця величина додатна - пересуваємо з кінця на початок, якщо від'ємна - 
навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]'''

def fnc(list_of_elem : list, shift):
   if shift < 0:
      return list_of_elem[abs(shift):] + list_of_elem[0: abs(shift)]
   if shift > 0:
      return list_of_elem[-shift:] + list_of_elem[0: -shift]


print(fnc([1, 2, 3, 4, 5], shift=1))
print(fnc([1, 2, 3, 4, 5], shift=-2))