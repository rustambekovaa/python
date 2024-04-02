class BaseUser:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        
        
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"



class User(BaseUser, Person):
    admin = 'admin'
    client = 'client'

    def __init__(self, username, first_name, last_name, password, email, age, role):
        
        super().__init__(username, password, email)
        super().__init__(first_name, last_name,age)
        # self.role = role
        if role == "admin" or role == "client" :
            self.role = role
        else:
            print("No this role!!!!")
            
    def get_role(self):
        return self.role
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name} {self.role}"

    
class AnonymousUser:
    def __init__(self):
        pass


user = [User("Akmaanai", "Akmaanai", "Rustambekova", "mirgul", "rustambekovaa15@gmail.com", 18, "client")]


class AuthSystem:    
    def __init__(self):
        self.is_authenticated = False
        self.user =AnonymousUser()
        self.key = None
        
    def login(self, username, password):
        if user.password == password:
            if user.username == username:
                self.is_authenticated = True
                print("Аутентификация прошла успешно!")
                print("Полное имя пользователя:", self.user.get_full_name())
                print("Роль пользователя:", self.user.get_role())
            else:
                print("Неправильный пароль!")
        else:
            self.user = None
            print("Пользователь с таким именем не найден!")


base = BaseUser("Akmaanai", 1234, "rustambekovaa15@gmail.com")
user = User("Akmaanai", "Akmaanai", "Rustambekova", 1234, "rustambekovaa15@gmail.com", 18, "client")
anon = AuthSystem()
anon.user = base
anon.login("Atanai", 12345)  # Пример неудачной аутентификации
anon.login("Akmaanai", 1234)  # Пример успешной аутентификации
