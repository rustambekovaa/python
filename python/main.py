# month = int(input("Ввеите число"))
# active = True
# if month == 1 and active == True :
#     print("январь")
# elif month == 2:
#     print("febral")
# elif month == 3:
#     print("mart")
# elif month == 4:
#     print("april")


# k =[['Maanai''2',],['Akmaanai','1'],['Tom'],['akmanai','0']]    
# k1 = {}
# for i in k:
#     if len(i)>=2:
#         key,values = i[0],i[1]
#         k1[key] = values
#     elif len(i)<=1:
#         key = i[0]   
#         k1[key] = None 
# print(k1)




dict = {}
while True:
    print("Введите один из вкладок \n 1. register \n 2. login \n 3. reset password \n0. quit ")
    register =int(input("Выберите: "))
    if register == 1:
        log = input("Login:")
        if log in dict:
            print("Такой логин существует")
            log = input("Login:")
            dict[log] = {}
        else:
            dict[log] = {}
        # dict[log] = {}
        print("Пароль должен иметь и буквы и число")
        # password = input("Password:")
        while True:
            password = input("Password:")
            if 8 >=len(password) >= 4:
                if  "#" in password and "-" in password and "*" in password:
                    print("«Пароль имеет не допустимые символы #-*")
                    # password = input("Password:")  
                elif password.isdigit():
                    print("«Ваш пароль имеет только цифры исправьте»")
                    # password = input("Password:")  
                elif password.isupper() or password.islower():
                    print("Ваш пароль не безопасный ")
                    # password = input("Password:")  
                else:
                    dict[log]["password"] = password
                    break
        number = input("Введите телефон номера с колом страны: ")
        if number.startswith("+996"):
            dict[log]["number"] = number
        else:
            print("Введите правилный номер!!!")
            number = input("Введите телефон номера с колом страны: ")
            dict[log]["number"] = number
        print(dict)
    elif register ==2:
        log1 = input("Login: ")
        password1 = input("password: ")
        for log1 in dict:
            if dict[log1]['password'] == password1:
                print("well come")
            else:
                print("ERROR")
    elif register == 3:
        log2 = input("Login:")
        number = input("number:")
        for log2 in dict:
            if dict[log1]['number'] == number:
                print(f" Ваш пароль {dict[log1]['password']}")
    elif register == 0:
        print("Вы закрыли программу")     
        break






# category={1:"breakfast",
#           2:"foods"
# }

# foods={"Pizza":{
#     # "category_id":1,
#     # "price":256
# }

# }

# while True:
#     choose=int(input("1:Добаление товара,\n2:Измнение товара,\n3:Удаление товара,\n4:Список товара,\n5:Категория товара,\n6:Добавление категории,\n0:Exit,\n ВЫБЕРИТЕ ОДИН ИЗ НИХ:"))
#     if choose == 1:
#         nameton = input("Вы выбрали вариант добаление товара \n Называние товара:")
