# Создаем декоратор
def my_decorator(func):
    def wrapper():
        print("Что-то происходит перед выполнением функции")
        func()  # Вызываем переданную функцию
        print("Что-то происходит после выполнения функции")
    return wrapper

# Определяем функцию, которую мы хотим декорировать
@my_decorator
def say_hello():
    print("Привет!")
say_hello()
# Декорируем функцию с помощью декоратора
# decorated_function = my_decorator(say_hello)

# # Вызываем декорированную функцию
# decorated_function()