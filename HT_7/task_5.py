'''Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих 
регістро-незалежних букв та цифр, які зустрічаються в рядку більше ніж 1 раз. 
Рядок буде складатися лише з цифр та букв (великих і малих). Реалізуйте обчислення 
за допомогою генератора в один рядок
    Example (input string -> result):
    "abcde" -> 0            # немає символів, що повторюються
    "aabbcde" -> 2          # 'a' та 'b'
    "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
    "indivisibility" -> 1   # 'i' присутнє 6 разів
    "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
    "aA11" -> 2             # 'a' і '1'
    "ABBA" -> 2             # 'A' і 'B' кожна двічі'''

def count_let(string):
	return len(set([let for let in string.upper() if string.upper().count(i) > 1 ]))

#print(count_let("abcde"))
#print(count_let("aabbcde"))
#print(count_let("aabBcde"))
#print(count_let("indivisibility"))