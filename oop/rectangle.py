class rectangle:
    def __init__(self,width,height) :
        self.width = width
        self.height = height
        print("The object is create!!!!")
    def calculate_area(self):
        print(f"The area of reqtanle is {self.width* self.height}")
        
area = rectangle(7,4)
area.calculate_area()

    