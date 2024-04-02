# class Animal:
    
#     def __init__(self,name):
#         self.name=name
        
#     def say(self):
#         pass
    
#     def info(self):
#         print(self.name,"Imya")
        
        
# class Cat(Animal): 
#     def __init__(self, name,color):
#         super().__init__(name)
#         self.color=color
        
#     def say(self):
#         print("myao")
        
#     def is_color(self):
#         print(f"{self.name},Svet {self.color}")    
     
     
# cat=Cat("Koshka","red")
# cat.is_color()
# cat.info()



class Workers:
    def __init__(self,work_name) -> None:
        self.work_name=work_name
    
    def work(self):
        print(self.work_name)    
        
class percon(Workers):
    def __init__(self, work_name,name,age):
        super().__init__(work_name)
        self.name = name
        self.age = age
    def result (self):
        print(f' name of work: {self.work_name} \n name: {self.name} \n age: {self.age}')
        
        
        
        
