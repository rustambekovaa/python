
# class Akount:
#     def __init__(self,username,password,age) -> None:
#         self.__username = username
#         self.__password = password
#         self.__age = age
    
#     @property
#     def username(self):
#         return self.__username   
    
#     @username.setter
#     def setname(self,name):
#         self.__username=name
#         return self.__username
    
    
    
    
# tom = Akount("tom23","123",19) 
# print(tom.username)
# tom.setname="New Name"
# print(tom.username)



class Bankomat:
        def __init__(self,user,password):
            self.__user = user
            self.__password = password
            self.__balance = 0
            
        def get_balance(self,passworld):
            if passworld == self.__password:
                print(self.__balance)
                
        def set_balance(self,passworld,money):
            if passworld == self.__password:
                self.__balance+= money
                # print(self.__balance)
            
        def rem_balance(self,passworld,rembal):
            if passworld == self.__password:
                self.__balance-=rembal
                # print(self.__balance)
        
ban=Bankomat("Akaamai",1234)
ban.get_balance(1234)
ban.set_balance(1234,5000)
ban.get_balance(1234)

ban.rem_balance(1234,4000)

ban.get_balance(1234)
