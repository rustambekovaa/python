class car:    
    def say_hello(self):
        print("Hello")
    
    def __init__(self,name,mark,year):
        self.name=name
        self.mark=mark
        self.year=year
        print("Обект создался")
    
    def diapley_info(self):
        print(f"name: {self.name},mark : {self.mark}, year: {self.year}")
        

    def quite(self):
        print("break") 

tom = car("Tesla","X8","2024")
tom.diapley_info()
tom.quite()