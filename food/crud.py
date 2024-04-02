# import json

# def add_data(choose):
#     if choose == 1:
#         num = input("num: ")
#         name = input("name: ")
#         age = input("age: ")
#         data = {
#             'num': num,
#             'name': name,
#             'age': age
#         }
#         with open("student.json", 'w+') as file:
#             try:
#                 existing_data = json.load(file)
#             except json.decoder.JSONDecodeError:
#                 existing_data = {}

#         existing_data[num] = data

#         with open("student.json", 'w') as save:
#             json.dump(existing_data, save)
#             print("Hurraaaa")

# choose = int(input("1) Add\n2) Edit\n3) Delete\n4) View\n"))
# add_data(choose)


# import json
# import os

# def add_data(choose):
#     if choose == 1:
#         num = input("num: ")
#         name = input("name: ")
#         age = input("age: ")
#         data = {
#             'num': num,
#             'name': name,
#             'age': age
#         }

#         if os.path.exists("student.json"):
#             with open("student.json", 'r') as file:
#                 try:
#                     existing_data = json.load(file)
#                 except json.decoder.JSONDecodeError:
#                     existing_data = {}
#         else:
#             existing_data = {}

#         existing_data[num] = data

#         with open("student.json", 'w') as save:
#             json.dump(existing_data, save)
#             print("Hurraaaa")

# choose = int(input("1) Add\n2) Edit\n3) Delete\n4) View\n"))
# add_data(choose)






import json

with open('foods.json', 'r+') as file:
    foods_object = file.read()
    python_object = json.loads(foods_object)
print(python_object)


while True:
    menu = int(input("1:Список продуктов \n2:Получение продукта по id \n3:Создание нового продукта \n4:Редактирование продукта по id \n5:Удаление продукта по id \n0:Выход \nВыберите что-то: "))
    if menu == 1:
        print(python_object)
    elif menu == 2:
        get_element = int(input("Введите id для того чтобы получить элемент: "))
        for i in python_object:
            if i.get('id') == get_element:
                print(i)
                break
        else:
            print("Нет такое ID")
    elif menu == 3:
        name_food = input("Введите название блюда: ")
        price_food = float(input("Введите цену: "))
        id_food = max(i.get('id') for i in python_object) + 1
        new_product = {"name": name_food, "price": price_food, "id": id_food}
        python_object.append(new_product)
    elif menu == 4:
        update_id = int(input("Введите id чтобы изменить"))
        for i in python_object:
            if i.get('id') == update_id:
                vybiray = int(input("Выберите то что хотите изменить: \n1:name \n2:price \n"))
                if vybiray == 1:
                    new_name = input("Введите новое название блюда: ")
                    i['name'] = new_name
                elif vybiray == 2:
                    new_price = int(input("Введите новую цену: "))
                    i['price'] = new_price
                    break
        else:
            print("Нет такое ID")
    elif menu == 5:
        delete_food = int(input("Введите id чтобы удалить этого блюда: "))
        for i in python_object:
            if i.get('id') == delete_food:
                python_object.remove(i)
    elif menu == 0:
        with open('foods.json', 'w', encoding='utf-8') as my_file:
            a = json.dump(python_object, my_file, indent=2, ensure_ascii=False)
        break
    else:
        print("Нет такой вариант")




