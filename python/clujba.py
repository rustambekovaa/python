# age = int(input("Age:"))
# name = input("Name:")
# toll = float(input("Toll:"))
# weiht = int(input("Weiht:"))

# if 18 <= age <= 25 and 170 <= toll <= 200 and 50 <= weiht <= 100:
#     print(f"{name},вы пригодны для службы в армии!!!!!!!")
# else:
#     print(f"{name},вы   не пригодны для службы в армии!!!!!!!")



# my_tuple = (10, 20, 30, 60, 50, 60, 70, 80, 90,60, 100)

# # Ищем значение 60 в кортеже, начиная с индекса 5
# index_value = my_tuple.index(60, 1)
# print(f"Индекс значения 60, начиная с индекса 1: {index_value}")


category={1:"breakfast",
            2:"foods"
    }

foods={}

while True:
    choose=int(input("1:Добаление товара,\n2:Измнение товара,\n3:Удаление товара,\n4:Список товара,\n5:Категория товара,\n6:Добавление категории,\n0:Exit,\n ВЫБЕРИТЕ ОДИН ИЗ НИХ:"))
    if choose == 1:
        nametovar = input("Вы выбрали вариант добаление товара \n Называние товара:")
        if nametovar in foods:
            print("Такой товар существует")
        else:
            print(category)
            catId = int(input("catId:"))
            if catId not in category:
                print("Такой категории не существует. Добавьте категорию сначала.")
            else:
                price = input("price:")
                foods[nametovar] ={"catId":catId,"price":price} 
                print(foods)
    elif choose ==2:
        wichtovar = input(f"Какой товар вы хотите изменить \n {list(foods.keys())} \n Напишите называние товара:")
        if wichtovar in foods:
            print(foods[wichtovar])
            print(category)
            newcat = int(input("Введите новую категорию для товара:"))
            if newcat not in category:
                print("Такой категории не существует. Добавьте категорию сначала.")
            else:
                newprice = input("Введите новую цену для товара:")
                foods[wichtovar] = {"catId":newcat,"price":newprice} 
                print(foods)
        else:
            print("Такого товара нету")
    elif choose ==3:
        deltovar = input(f"Вы выбрали Удаление товара \n {list(foods.keys())} \n Выберите один из имя с верхной списки :")    
        if deltovar in foods:
            del foods[deltovar] 
            print(f"Товар , {deltovar} удалено ")
            print(foods)
        else:
            print(f"Товар с именем '{deltovar}' не найден.")
    elif choose ==4:
        print(foods)
    elif choose ==5:
        for i in foods:
            print(foods[i]["catId"])
    elif choose ==6:
        catadd = int(input("Категория:"))
        if catadd in category:
            print("Такой котегории существует")
        else:
            name = input("name:")
            category[catadd] =name 
            print(category)
    elif choose ==0:
        print("Вы закрыли программу")     
        break
            
            
                
            
                
                
            
            
        
