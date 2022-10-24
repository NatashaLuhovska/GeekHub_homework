'''На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів 
   (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись
    валідатором, перевірить ці дані і надрукує для кожної пари значень 
    відповідне повідомлення, наприклад:

      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)'''

users_list = [('vasya', '1234werQWE'), ('va', '1234werQWE'), ('vasya', '1234we'), 
			  ('vasya', 'rtyewerQWE'), ('vasya', '122334QWE'), ('vasya', '1234werty')]

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

for user in users_list:
   status = "OK"
   try:
      valid_username_pass(user[0], user[1])
   except LenNameException:
      status = "The name must be at least 3 characters and no more than 50."
   except LenPassException:
      status = "The password must be at least 8 characters long."
   except DigPassException:
      status = "The password must have at least one digit"
   except UpLowPassException:
      status = "Password must have at least one character in upper and lower case!"
   finally:
      print(f'Name: {user[0]}')
      print(f'Password: {user[1]}')
      print(f'Status: {status}')
      print('-------------------')


