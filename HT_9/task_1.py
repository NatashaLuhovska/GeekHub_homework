'''Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних у відповідних таблицях. Більше ніяких файлів. 
    Якщо в попередньому завданні ви добре продумали структуру програми то у вас не виникне проблем 
    швидко адаптувати її до нових вимог.
    - на старті додати можливість залогінитися або створити нового користувача (при створенні нового 
    користувача, перевіряється відповідність логіну і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
    - в таблиці з користувачами також має бути створений унікальний користувач-інкасатор, який матиме 
    розширені можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
    - банкомат має власний баланс
    - кількість купюр в банкоматі обмежена (тобто має зберігатися номінал та кількість). Номінали 
    купюр - 10, 20, 50, 100, 200, 500, 1000
    - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
    - користувач через банкомат може покласти на рахунок лише суму кратну мінімальному номіналу що 
    підтримує банкомат. В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5).
     Але це не має впливати на баланс/кількість купюр банкомату, лише збільшується баланс користувача 
     (моделюємо наявність двох незалежних касет в банкоматі - одна на прийом, інша на видачу)
    - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
    - при неможливості виконання якоїсь операції - вивести повідомлення з причиною (невірний логін/пароль, 
    недостатньо коштів на рахунку, неможливо видати суму наявними купюрами тощо.)
    - файл бази даних з усіма створеними таблицями і даними також додайте в репозиторій, 
    що б ми могли його використати'''


 #  sqlite_connection = sqlite3.connect('ATM_2_0.db')
 #   sqlite_create_table_query = '''CREATE TABLE Users (
 #                               id INTEGER PRIMARY KEY,
 #                               login TEXT NOT NULL UNIQUE,
 #                               password text NOT NULL,
 #                               balance REAL NOT NULL);'''

 #    sqlite_create_table_query = '''CREATE TABLE Transactions (
 #                              id INTEGER PRIMARY KEY,
 #                               login TEXT NOT NULL,
 #                               time_operation datetime,
 #                               type text NOT NULL,
 #                              amount_of_money REAL NOT NULL);'''

 #sqlite_create_table_query = '''CREATE TABLE Collector_table (
 #                              id INTEGER PRIMARY KEY,
 #                              time_operation datetime,
 #                              operation text NOT NULL);'''


#sqlite_create_table_query = '''CREATE TABLE Bills (
#                                id INTEGER PRIMARY KEY,
#                                nominal TEXT NOT NULL UNIQUE,
#                                count INTEGER NOT NULL);'''

#sqlite_create_table_query = '''CREATE TABLE ATM_operations (
#                                id INTEGER PRIMARY KEY,
#                                time_operation datetime,
#                                login TEXT NOT NULL,
#                                operation text NOT NULL);'''

######################### IMPORT #################################

import datetime
import sqlite3


###################################################################

####################### CREAT NEW USER ############################

def valid_username_pass(username: str, password: str):
   if len(username) < 3 or len(username) >= 50:
      print("Логін повинно бути не меншим за 3 символа і не більшим за 50!")
      return False
   if len(password) < 8:
      print("Пароль повинен бути не меншим за 8 символів!")
      return False
   if not any(elem.isdigit() for elem in password):
      print("Пароль повинен мати хоча б одну цифру!")
      return False
   if not any(elem.islower() for elem in password) or not any(elem.isupper() for elem in password):
      print("Пароль повинен мати хоча б один символ у верхньому та нижньому регістрах!")
      return False
   else:
      return True


def check_in_system(name):
    if cursor.execute('''SELECT * FROM Users WHERE login='{}' '''.format(name)).fetchall():
        print('Такий користувач є в системі!')
        return True
    else:
        return False

def creat_new_user():
    name = input("Введіть Ваше логін: \n")
    password = input("Введіть пароль: \n")
    
    while not valid_username_pass(name, password) or check_in_system(name):
        print("Якщо ви бажаєте продовжити реєстрацію натисніть - 1, інакше натисніть - 0.")
        if input() == '0':
            return False
        if check_in_system(name):
            print('Такий користувач є в системі!')
            name = input("Введіть Ваше логін: \n")
            password = input("Введіть пароль: \n")
        if not valid_username_pass(name, password):
            name = input("Введіть Ваше логін: \n")
            password = input("Введіть пароль: \n")

    if valid_username_pass(name, password):
        user_id = len(cursor.execute("SELECT * FROM Users").fetchall())+1
        cursor.execute("INSERT INTO Users (id, login, password, balance) VALUES \
            (?,?,?,?)", (user_id, name, password, 0))
        sqlite_connection.commit()
        operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall())+1
        cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
            (?,?,?,?)", (operation_id, datetime.datetime.now(), name, 'creat new user'))
        sqlite_connection.commit()
        return name

########################### LOGIN USER #########################################

def login_user():
    for i in range(3):
        name = input("Ввведіть ім'я : ")
        password = input("Введіть пароль : ")
        if cursor.execute('''SELECT * FROM Users WHERE login='{}' AND password='{}' '''.format(name,password)).fetchall():
            print(f"Вітаємо {name}!")
            operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall())+1
            cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
                (?,?,?,?)", (operation_id, datetime.datetime.now(), name, 'login user'))
            sqlite_connection.commit()
            return name
        else:
            print(f"Не правильно введені дані, у вас лишилося {2 - i} спроби")
            return False

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
############################### CHEK BALANCE ##################################

def chek_balance(name):
    operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall())+1
    cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
        (?,?,?,?)", (operation_id, datetime.datetime.now(), name, 'chek balance'))
    sqlite_connection.commit()
    return cursor.execute('''SELECT balance FROM Users WHERE login='{}' '''.format(name)).fetchall()[0][0]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
############################## WITHDRAW CASH ##################################

def withdraw_cash(name):
    cash = int(input('Яку суму ви бажаєте зняти (тільки додатні числа)\n'))
    if cash < 0:
        return "Ви не можете знімати від'ємні суми!"
    balance = cursor.execute('''SELECT balance FROM Users WHERE login='{}' '''.format(name)).fetchall()[0][0]
    if cash > balance:
        print("Сума перевищує ваш поточний баланс на карті.")
        return "Змініть суму, на ту, що не перевищує Ваш баланс. "
    balance_ATM = cursor.execute('''SELECT count FROM Bills WHERE nominal='{}' '''.format("Total")).fetchall()[0][0]
    if cash > balance_ATM:
        print("Сума перевищує наш поточний баланс в банкоматі.")
        return "Змініть суму, ту, що не перевищує баланс. "
    balance -= cash
    cursor.execute('''UPDATE Users SET balance='{}' WHERE login='{}' '''.format(balance, name))
    sqlite_connection.commit()
    transaction_id = len(cursor.execute("SELECT * FROM Transactions").fetchall())+1
    cursor.execute("INSERT INTO Transactions (id, login, time_operation, type, amount_of_money) VALUES \
        (?,?,?,?,?)", (transaction_id, name, datetime.datetime.now(), 'withdraw cash', cash))
    sqlite_connection.commit()
    operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall())+1
    cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
        (?,?,?,?)", (operation_id, datetime.datetime.now(), name, 'withdraw cash'))
    sqlite_connection.commit()
    return "Операція успішна!"


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
########################### TOP UP ACCOUNT ####################################

def top_up_account(name):
    cash = int(input('Яку суму ви бажаєте покласти на рахунок? (тільки додатні числа) \n'))
    if cash < 0:
        return "Ви не можете додавати від'ємні значення!"
    balance = balance = cursor.execute('''SELECT balance FROM Users WHERE login='{}' '''.format(name)).fetchall()[0][0]
    new_cash = cash // 10 *10 
    balance += new_cash  
    cursor.execute('''UPDATE Users SET balance='{}' WHERE login='{}' '''.format(balance, name))
    sqlite_connection.commit()
    transaction_id = len(cursor.execute("SELECT * FROM Transactions").fetchall())+1
    cursor.execute("INSERT INTO Transactions (id, login, time_operation, type, amount_of_money) VALUES \
        (?,?,?,?,?)", (transaction_id, name, datetime.datetime.now(), 'top up account', new_cash))
    sqlite_connection.commit()
    operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall())+1
    cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
        (?,?,?,?)", (operation_id, datetime.datetime.now(), name, 'top up account'))
    sqlite_connection.commit()
    return f"Операція успішна! На рахунок зараховано: {new_cash}. Решта: {cash - new_cash}"




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
########################### COLLECTOR FUNTIONS ################################

def count_total():
    total = 0
    for row in cursor.execute("SELECT * FROM Bills"):
        if row[1] != "Total":
            total += int(row[1]) * row[2]
    cursor.execute('''UPDATE Bills SET count='{}' WHERE nominal='{}' '''.format(total, "Total"))
    sqlite_connection.commit()  

def chek_bills():
    print(f'{"Bill":15} {"Count"}')
    for row in cursor.execute("SELECT * FROM Bills"):
        print(f'{row[1]:15} {row[2]}')
    operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall())+1
    cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
        (?,?,?,?)", (operation_id, datetime.datetime.now(), 'admin', 'chek bills'))
    sqlite_connection.commit()



def change_bill_count():
    bill = input("Введіть номінал купюри : \n")
    count_bill = int(input("Введіть кількість купюр: \n"))
    cursor.execute('''UPDATE Bills SET count='{}' WHERE nominal='{}' '''.format(count_bill, bill))
    sqlite_connection.commit()
    count_total()
    change_bill_id = len(cursor.execute("SELECT * FROM Collector_table").fetchall())+1
    cursor.execute("INSERT INTO Collector_table (id, time_operation, operation) VALUES \
        (?,?,?)", (change_bill_id, datetime.datetime.now(), f'change bill {bill} count {count_bill}'))
    sqlite_connection.commit()
    operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall())+1
    cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
        (?,?,?,?)", (operation_id, datetime.datetime.now(), 'admin', 'change bill count'))
    sqlite_connection.commit()


  




##############################################################################################
##############################################################################################

def start():
    print("Вітаємо!")
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%') 
    print("Яку операцію бажаєте виконати?")
    print('**************************') 
    operations = """            
    Увійти             --  Натисніть 1
    Зареєструватися    --  Натисніть 2
    """
    print(operations)
    print('**************************') 
    operation = input()
    if operation == '1':
        name = login_user()
    elif operation == '2':
        name = creat_new_user()

    if not name:
        print("Зверніться, будь ласка, в банк, для вирішення вашої проблеми.")
        return None
    elif name == 'admin':
        while True:
            print('&&&&&&&&&&&&&&&&&&&&&&&&& \n') 
            print("Яку операцію бажаєте виконати?")
            print('**************************') 
            operations = """            
            Перевірити наявні купюри      --  Натисніть 1
            Змінити кількість купюр       --  Натисніть 2
            Вийти                         --  Натисніть 0 
            """
            print(operations)
            print('**************************') 
            operation = input()
            if operation == '1':
                chek_bills()
            elif operation == '2':
                change_bill_count()
            elif operation == '0':
                print('До нових зустрічей!')
                return "Дякуємо, за Вашу роботу!"
            else:
                print("Не правильно введене значення!")
            print('&&&&&&&&&&&&&&&&&&&&&&&&& \n')
    else:
        while True:
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%') 
            print("Яку операцію бажаєте виконати?")
            print('**************************') 
            operations = """            
            Зняти готівку      --  Натисніть 1
            Поповнити рахунок  --  Натисніть 2
            Переглянути баланс --  Натисніть 3
            Вийти              --  Натисніть 0 
            """
            print(operations)
            print('**************************') 
            operation = input()
            if operation == '1':
                print(withdraw_cash(name))
            elif operation == '2':
                print(top_up_account(name))
            elif operation == '3':
                print(f"На вашому рахунку {chek_balance(name)} грн.")
            elif operation == '0':
                print('До нових зустрічей!')
                return "Дякуємо, що Ви обрали наш банк!"
            else:
                print("Не правильно введене значення!")
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%')






try:
    sqlite_connection = sqlite3.connect('ATM_2_0.db')
    cursor = sqlite_connection.cursor()

    print(start())

    cursor.close()

except sqlite3.Error as error:
    print("Помилка при подключенні до sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("З'єднання з SQLite закрито")







