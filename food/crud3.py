category = { 
    1:"breakfast", 
    2:"foods" 
} 
x=3 
zna="lunch" 
category[x] = zna 
print(category) 
foods = {} 
 
CHOICE = f""" 
    1:"Добавления товара, 
    2:"Изменение товара, 
    3:"Удаление товара, 
    4:"Список товара, 
    5:"Категория товара, 
    6:"Добавление категории, 
    0:"Exit 
""" 
listt = [] 
 
while True: 
    print("Выберите один из", CHOICE) 
    menu = int(input("Введите чилсо ")) 
    if menu == 1: 
        print("Вы выбрали вариант добавление товара") 
        name = input("Название товара  ") 
        if not name in foods: 
                price = int(input('Цена  ')) 
                cat = int(input("1) \n2) \n")) 
                if cat in category: 
                   foods[name] = {'cat': cat, 'price':price} 
                   print("Успешно добавлен", foods[name]) 
        else: 
             print("error") 
    if menu == 2: 
       print("Вы выбрали изменение товара") 
       name1 = input("Напиши название товара  ") 
       if name1 in foods: 
            print(foods[name1]) 
            newcategory = int(input("Введите новую категория для товара  ")) 
            newprice = int(input("Введите новую цену для товара  ")) 
            foods[name1] = {'cat': newcategory, 'price': newprice} 
            print("Успешно изменилось", foods[name1]) 
       else: 
            print("error") 
    if menu == 3: 
         print("Вы выбрали удаление товара")     
         name2 = input("Напиши название товара для удаление  ") 
         if name2 in foods: 
              del foods[name2] 
              print("Успешно удалено") 
         else: 
              print("Товар с таким названием не найден") 
    if menu == 4: 
         print("Вы выбрали список товара") 
         result_list = list(foods) 
         print('Список товаров:', result_list) 
    if menu == 0: 
         print("Программа окончена досвидания") 
         break