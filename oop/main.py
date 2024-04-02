class Person:    
    def say_hello(self):
        print("Hello")
    
    def __init__(self,name,age):
        self.imya=name
        self.vpzrast=age
        print("Обект создался")
    
    def diapley_info(self):
        print(f"name: {self.imya},age : {self.vpzrast}")
        

def printing():
    return "text"

tom = Person("Belek","21")
tom.work="PROLAB"
tom.value()
# andrey=Person("Andrey",23)
# andrey.value()
# print(andrey.work)