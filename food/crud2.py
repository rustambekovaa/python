import json 
 
import uuid 
 
 
def len_json(): 
    with open('data.json', 'r+') as aut: 
        h = json.load(aut) 
    lst = [] 
    for i in h["users"]: 
        lst.append(i) 
    return len(lst) 
 
 
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
        return f'{self.last_name} {self.last_name}' 
 
 
class User(BaseUser, Person): 
 
    def __init__(self, username, name, last_name, password, email, age, role): 
        BaseUser.__init__(self, username, password=password, email=email) 
        Person.__init__(self, name, last_name=last_name, age=age) 
        self.getrole = role 
 
    def get_full_name(self): 
        return super().get_full_name() + self.get_role 
 
    def get_base(self): 
        with open('data.json', 'r+') as f: 
            d = json.load(f) 
        lstuser = [] 
        lstpassw = [] 
        lstkey = [] 
        for i in d["users"]: 
            lstuser.append(i['username']) 
            lstpassw.append(i['password']) 
            lstkey.append(i['key']) 
        return {'user': lstuser, 'password': lstpassw, 'key': lstkey} 
 
    def add_user(self): 
        jj = uuid.uuid4().hex 
        h = { 
            "id": len_json() + 1, 
            "username": self.username, 
            "first_name": self.first_name, 
            "last_name": self.last_name, 
            "password": self.password, 
            "email": self.email, 
            "age": self.age, 
            "role": self.getrole, 
            "key": jj, 
        } 
        with open('data.json', 'r+') as f: 
            d = json.load(f) 
        d["users"].append(h) 
        with open('data.json', 'w', encoding='utf8') as aut: 
            json.dump(d, aut, ensure_ascii=False, indent=2) 
        return jj 
 
    def get_role(self): 
        return f'{self.getrole}, {self.first_name}' 
 
 
class AnonymousUser(User): 
    pass 
 
 
class AuthSystem(User): 
    def __init__(self): 
        self.is_authenticated = None 
        self.user = None 
        self.key = None 
 
    def login(self, username, password): 
        users = self.get_base() 
        id = 0 
        for item in users['user']: 
            if item == username: 
                id = users['user'].index(item) 
        if username in users['user'] and password in users['password']: 
            print(users['user']) 
            self.is_authenticated = True 
            return users['key'][id] 
        else: 
            self.is_authenticated = False 
            return False 
 
    def authenticate(self, key): 
        with open('data.json', 'r+') as f: 
            d = json.load(f) 
        w = 0 
        for i in d["users"]: 
            if i['key'] == key: 
                w = 1 
                return f'{i["first_name"]} {i["last_name"]} {i["role"]}' 
        if w == 0: 
            return False 
 
 
j = AuthSystem() 
# print(j.login('pauk','12345678')) 
 
lst = ['admin', 'manager', 'programmer'] 
while True: 
    print("1добавить пользователь\n2войти\n4authenticate\n3exit") 
    n = int(input()) 
    if n == 1: 
        username = input('username:') 
        name = input('first_name:') 
        last_name = input('last_name') 
        password = input("password:") 
        if len(password) < 8: 
            print('вы вели не правильный пароль(') 
            while len(password) < 8: 
                password = input("password:") 
        email = input('email:') 
        age = input("age:") 
        role = int(input('role\n1admin\n2manager\n3Programmer:')) 
        if role > 3 and role > 0: 
            while role > 3 and role > 0: 
                role = int(input('role\n1admin\n2manager\n3Programmer:')) 
        role = lst[role - 1] 
        new_user = User(username, name, last_name, password, email, age, role)
        print(new_user.add_user()) 
    elif n == 2: 
        username = input('username:') 
        password = input("password:") 
        g = AuthSystem() 
        print(g.login(username, password)) 
    elif n == 4: 
        key = input('key:') 
        g = AuthSystem() 
        print(g.authenticate(key)) 
    elif n == 3: 
        print('Досвидания') 
        break