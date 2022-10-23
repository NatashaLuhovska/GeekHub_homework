'''Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параметрів не відповідає вимогам - породити 
   виключення із відповідним текстом.'''

class LenNameException(Exception):
   pass

class LenPassException(Exception):
   pass

class DigPassException(Exception):
   pass

class UpLowPassException(Exception):
   pass


def valid_username_pass(username: str, password: str):
   if len(username) < 3 or len(username) >= 50:
      raise LenNameException("Ім'я повинно бути не меншим за 3 символа і не більшим за 50!")
   if len(password) < 8:
      raise LenPassException("Пароль повинен бути не меншим за 8 символів!")
   if not any(elem.isdigit() for elem in password):
      raise DigPassException("Пароль повинен мати хоча б одну цифру!")
   if not any(elem.islower() for elem in password) or not any(elem.isupper() for elem in password):
      raise UpLowPassException("Пароль повинен мати хоча б один символ у верхньому та нижньому регістрах!")
   else:
      return True

#print(valid_username_pass('Vwr','34erQW2345'))
#print(valid_username_pass('Vw','34erQW2345'))
#print(valid_username_pass('Vwr','34er5'))
#print(valid_username_pass('Vwr','34er2345'))