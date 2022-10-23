'''Створіть функцію, всередині якої будуть записано СПИСОК із п'яти користувачів
 (ім'я та пароль). 
Функція повинна приймати три аргументи: два - обов'язкових
 (<username> та <password>) і третій - необов'язковий параметр
  <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено правильну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція повертає False
        якщо silent == False - породжується виключення 
        LoginException (його також треба створити =))'''

class LoginException(Exception):
  pass

def login_def(username : str, password : str, silent=False):
  users_list = [('Tom', '234323'), ('Nick', '34567'), ('Anna', 'd45678'), ('No', 'sdfr32344'), ('Denis', '23467784')]
  for i in users_list:
    if i[0] == username and i[1] == password:
      return True
    elif silent == True:
      return False
    else:
      raise LoginException("Введено неправильну пару ім'я/пароль!!!")

#print(login_def('No', 'sdfr32344'))
#print(login_def('To', '234323', silent=True))
#print(login_def('To', '234323'))