'''Банкомат 3.0
- реалізуйте видачу купюр за логікою видавання найменшої кількості купюр, але в межах наявних в 
банкоматі. Наприклад: 2560 --> 2х1000, 1х500, 3х20. Будьте обережні з "жадібним алгоритмом"! 
Видані купюри також мають бути “вилучені” з банкомату. Тобто якщо до операції в банкоматі 
було 5х1000, 5х500, 5х20 - має стати 3х1000, 4х500, 2х20.
- як і раніше, поповнення балансу користувача не впливає на кількість купюр. Їх кількість 
може змінювати лише інкасатор.
- обов’язкова реалізація таких дій (назви можете використовувати свої):

 При запускі
   Вхід
   Реєстрація (з перевіркою валідності/складності введених даних)
   Вихід

 Для користувача
   Баланс
   Поповнення
   Зняття
   Історія транзакцій
   Вихід на стартове меню

 Для інкасатора
   Наявні купюри/баланс тощо
   Зміна кількості купюр
   Повна історія операцій по банкомату (дії всіх користувачів та інкасаторів)
   Вихід на стартове меню

- обов’язкове дотримання РЕР8 (якщо самостійно ніяк, то https://flake8.pycqa.org/en/latest/ вам в допомогу)
- (опціонально) не лініться і придумайте якусь свою особливу фішку/додатковий функціонал, але 
при умові що основне завдання виконане'''


import datetime
import sqlite3
import random


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
    if cursor.execute('''SELECT * FROM Users WHERE login= ? ''', (name,)).fetchall():
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
        user_id = len(cursor.execute("SELECT * FROM Users").fetchall()) + 1
        cursor.execute("INSERT INTO Users (id, login, password, balance) VALUES \
            (?,?,?,?)", (user_id, name, password, 0))
        sqlite_connection.commit()
        operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall()) + 1
        cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
            (?,?,?,?)", (operation_id, datetime.datetime.now(), name, 'creat new user'))
        sqlite_connection.commit()
        return name


def login_user():
    for i in range(3):
        name = input("Ввведіть ім'я : ")
        password = input("Введіть пароль : ")
        if cursor.execute('''SELECT * FROM Users WHERE login= ? AND password= ? ''', (name, password)).fetchall():
            print(f"Вітаємо {name}!")
            operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall())+1
            cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
                (?,?,?,?)", (operation_id, datetime.datetime.now(), name, 'login user'))
            sqlite_connection.commit()
            return name
        else:
            print(f"Не правильно введені дані, у вас лишилося {2 - i} спроби")
    return False


def chek_balance(name):
    operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall()) + 1
    cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
        (?,?,?,?)", (operation_id, datetime.datetime.now(), name, 'chek balance'))
    sqlite_connection.commit()
    return cursor.execute('''SELECT balance FROM Users WHERE login= ? ''', (name,)).fetchall()[0][0]


def get_bills():
    bills = {}
    for row in cursor.execute("SELECT * FROM Bills"):
        if row[1] != 'Total':
            bills[row[1]] = row[2]
    return bills


def bills_available(bills):
    bills_avail = []
    for key, values in bills.items():
        if values > 0 :
            bills_avail.append(int(key))
    return bills_available


def bills_for_issuance(num, bills):
    bills_avail = []
    for key, values in bills.items():
        if values > 0 :
            bills_avail.append(int(key))
    bills_avail.sort(reverse=True)
    total = num
    while total != 0 and bills_avail != []:
        total = num
        new_bills = {}
        bills_issuance = {}
        for bill in bills_avail:
            if total // bill > 0:
                if bills[str(bill)] >= total // bill:
                    new_bills[str(bill)] = bills[str(bill)] - total // bill
                    bills_issuance[str(bill)] = total // bill
                    total = total - total // bill * bill
                elif bills[str(bill)] < total // bill:
                    new_bills[str(bill)] = 0
                    bills_issuance[str(bill)] = bills[str(bill)]
                    total = total - bills[str(bill)] * bill
            if total == 0:
                print("Виконано успішно!")
                return bills_issuance
        bills_avail.remove(max(bills_avail))
    if total != 0:
        print("Банкомат не має необхідної кількості купюр для видачі вказаної суми.")
        return False


def withdraw_cash(name):
    cash = int(input('Яку суму ви бажаєте зняти (тільки додатні числа, кратні 10)\n'))
    if cash < 0:
        return "Ви не можете знімати від'ємні суми!"
    if cash % 10 != 0:
        return "Банкомат не має купюр номіналом меншим 10-ти грн!"
    balance = cursor.execute('''SELECT balance FROM Users WHERE login= ? ''', (name,)).fetchall()[0][0]
    if cash > balance:
        print("Сума перевищує ваш поточний баланс на карті.")
        return "Змініть суму, на ту, що не перевищує Ваш баланс. "
    balance_ATM = cursor.execute('''SELECT count FROM Bills WHERE nominal= ? ''', ("Total",)).fetchall()[0][0]
    if cash > balance_ATM:
        print("Сума перевищує наш поточний баланс в банкоматі.")
        return "Змініть суму, ту, що не перевищує баланс. "
    bills = get_bills()
    bills_for_iss = bills_for_issuance(cash, bills)
    if not bills_for_iss:
        return "Оберіть іншу суму!"
    print('Отримайте: ')
    for k, v in bills_for_iss.items():
        print(f'{v} банкнот, номіналом {k} грн')
        new = cursor.execute('''SELECT count FROM Bills WHERE nominal= ? ''', (str(k),)).fetchall()[0][0]
        cursor.execute('''UPDATE Bills SET count= ? WHERE nominal= ? ''', (new - v, str(k)))
        sqlite_connection.commit()
    count_total()
    balance -= cash
    cursor.execute('''UPDATE Users SET balance= ? WHERE login= ? ''', (balance, name))
    sqlite_connection.commit()
    transaction_id = len(cursor.execute("SELECT * FROM Transactions").fetchall()) + 1
    cursor.execute("INSERT INTO Transactions (id, login, time_operation, type, amount_of_money) VALUES \
        (?,?,?,?,?)", (transaction_id, name, datetime.datetime.now(), 'withdraw cash', cash))
    sqlite_connection.commit()
    operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall()) + 1
    cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
        (?,?,?,?)", (operation_id, datetime.datetime.now(), name, 'withdraw cash'))
    sqlite_connection.commit()
    return "Операція успішна!"


def top_up_account(name):
    cash = int(input('Яку суму ви бажаєте покласти на рахунок? (тільки додатні числа) \n'))
    if cash < 0:
        return "Ви не можете додавати від'ємні значення!"
    balance = cursor.execute('''SELECT balance FROM Users WHERE login= ? ''', (name,)).fetchall()[0][0]
    new_cash = cash // 10 *10 
    balance += new_cash  
    cursor.execute('''UPDATE Users SET balance= ? WHERE login= ? ''', (balance, name))
    sqlite_connection.commit()
    transaction_id = len(cursor.execute("SELECT * FROM Transactions").fetchall()) + 1
    cursor.execute("INSERT INTO Transactions (id, login, time_operation, type, amount_of_money) VALUES \
        (?,?,?,?,?)", (transaction_id, name, datetime.datetime.now(), 'top up account', new_cash))
    sqlite_connection.commit()
    operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall()) + 1
    cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
        (?,?,?,?)", (operation_id, datetime.datetime.now(), name, 'top up account'))
    sqlite_connection.commit()
    return f"Операція успішна! На рахунок зараховано: {new_cash}. Решта: {cash - new_cash}"


def chek_user():
    user = input("Введіть ім'я користувача: ")
    if cursor.execute('''SELECT * FROM Users WHERE login= ? ''', (user, )).fetchall():
        return user
    else:
        return False


def top_up_other_account(user, name):
    cash = int(input('Яку суму ви бажаєте покласти на рахунок? (тільки додатні числа) \n'))
    if cash < 0:
        return "Ви не можете додавати від'ємні значення!"
    balance = cursor.execute('''SELECT balance FROM Users WHERE login= ? ''', (name,)).fetchall()[0][0]
    new_cash = cash // 10 *10 
    balance += new_cash  
    cursor.execute('''UPDATE Users SET balance= ? WHERE login= ? ''', (balance, name))
    sqlite_connection.commit()
    transaction_id = len(cursor.execute("SELECT * FROM Transactions").fetchall()) + 1
    cursor.execute("INSERT INTO Transactions (id, login, time_operation, type, amount_of_money) VALUES \
        (?,?,?,?,?)", (transaction_id, name, datetime.datetime.now(), f'top up account from {user}', new_cash))
    sqlite_connection.commit()
    operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall()) + 1
    cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
        (?,?,?,?)", (operation_id, datetime.datetime.now(), name, f'top up account from {user}'))
    sqlite_connection.commit()
    return f"Операція успішна! На рахунок зараховано: {new_cash}. Решта: {cash - new_cash}"


def print_user_transactions(name):
    for row in cursor.execute('''SELECT * FROM Transactions WHERE login= ? ''', (name,)):
        print(row)


def count_total():
    total = 0
    for row in cursor.execute("SELECT * FROM Bills"):
        if row[1] != "Total":
            total += int(row[1]) * row[2]
    cursor.execute('''UPDATE Bills SET count= ? WHERE nominal= ? ''', (total, "Total"))
    sqlite_connection.commit()  


def chek_bills():
    print(f'{"Bill":15} {"Count"}')
    for row in cursor.execute("SELECT * FROM Bills"):
        print(f'{row[1]:15} {row[2]}')
    operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall()) + 1
    cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
        (?,?,?,?)", (operation_id, datetime.datetime.now(), 'admin', 'chek bills'))
    sqlite_connection.commit()


def change_bill_count():
    bill = input("Введіть номінал купюри : \n")
    count_bill = int(input("Введіть кількість купюр: \n"))
    cursor.execute('''UPDATE Bills SET count= ? WHERE nominal= ? ''', (count_bill, bill))
    sqlite_connection.commit()
    count_total()
    change_bill_id = len(cursor.execute("SELECT * FROM Collector_table").fetchall()) + 1
    cursor.execute("INSERT INTO Collector_table (id, time_operation, operation) VALUES \
        (?,?,?)", (change_bill_id, datetime.datetime.now(), f'change bill {bill} count {count_bill}'))
    sqlite_connection.commit()
    operation_id = len(cursor.execute("SELECT * FROM ATM_operations").fetchall()) + 1
    cursor.execute("INSERT INTO ATM_operations (id, time_operation, login, operation) VALUES \
        (?,?,?,?)", (operation_id, datetime.datetime.now(), 'admin', 'change bill count'))
    sqlite_connection.commit()


def print_ATM_operations():
    for row in cursor.execute("SELECT * FROM ATM_operations"):
        print(row)


def get_prediction():
    with open('text.txt', 'rt') as freading:
        prediction = []
        lines = freading.readlines()
        for line in lines:
            prediction.append(line)
    return prediction[random.randint(0, 104)]


def menu_1():
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n')
    print('{:^50}'.format("Вітаємо! \n"))
    while True:
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n') 
        print("Яку операцію бажаєте виконати? \n")
        print('*************************************************** \n') 
        operations = """            
        Увійти             --  Натисніть 1
        Зареєструватися    --  Натисніть 2
        Вийти              --  Натисніть 0
         """
        print(operations)
        print('***************************************************') 
        operation = input()
        if operation == '1':
            name = login_user()
            return name
        elif operation == '2':
            name = creat_new_user()
            return name
        elif operation == '0':
            print("#####################################################")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
            print('{:^50}'.format("Передбачення дня: \n"))
            print('{:^50}'.format(get_prediction()),'\n')
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print("#####################################################")
            return "Exit"
        else:
            print("Не правильно введене значення!")


def menu_for_admin():
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& \n') 
    print("Яку операцію бажаєте виконати?")
    print('********************************************************* \n') 
    operations = """            
    Перевірити наявні купюри             --  Натисніть 1
    Змінити кількість купюр              --  Натисніть 2
    Повна історія операцій по банкомату  --  Натисніть 3
    Повернутися на головне меню          --  Натисніть 0 
    """
    print(operations)
    print('********************************************************* ') 
    operation = input()
    if operation == '1':
        chek_bills()
    elif operation == '2':
        change_bill_count()
    elif operation == '3':
    	print_ATM_operations()
    elif operation == '0':
        print('До нових зустрічей!')
        return "Main menu"
    else:
        print("Не правильно введене значення!")
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& \n')


def menu_for_users(name):
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n') 
    print("Яку операцію бажаєте виконати?")
    print('*********************************************************** \n') 
    operations = """            
    Зняти готівку                        --  Натисніть 1
    Поповнити рахунок                    --  Натисніть 2
    Переглянути баланс                   --  Натисніть 3
    Повна історія транзакцій             --  Натисніть 4
    Поповнити рахунок іншого користувача --  Натисніть 5
    Повернутися на головне меню          --  Натисніть 0 
    """
    print(operations)
    print('***********************************************************') 
    operation = input()
    if operation == '1':
        print(withdraw_cash(name))
    elif operation == '2':
        print(top_up_account(name))
    elif operation == '3':
        print(f"На вашому рахунку {chek_balance(name)} грн.")
    elif operation == '4':
    	print_user_transactions(name)
    elif operation == '5':
        new_user = chek_user()
        if new_user:
            print(top_up_other_account(name, new_user))
        else:
            print("Такого користувача не існує в системі.")
    elif operation == '0':
        print('До нових зустрічей!')
        return "Main menu"
    else:
        print("Не правильно введене значення!")
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n')


def start():
    while True:
        name = menu_1()
        if not name:
            print("Зверніться, будь ласка, в банк, для вирішення вашої проблеми.")
            return None
        elif name == "Exit":
            return "Роботу завершено!"
        elif name == 'admin':
            while True:
                result = menu_for_admin()
                if result == "Main menu":
                    break
        else:
            while True:
                result = menu_for_users(name)
                if result == "Main menu":
                    break


try:
    sqlite_connection = sqlite3.connect("ATM_2_0.db")
    cursor = sqlite_connection.cursor()
    print(start())
    cursor.close()
    sqlite_connection.close()
except sqlite3.Error as error:
    print("Помилка при подключенні до sqlite", error)
except Exception as err:
    print("Виникла помилка: ", err)
    print("Банкомат тимчасово не працює.")
else:
    print("Роботу з банкоматом завершено!")
