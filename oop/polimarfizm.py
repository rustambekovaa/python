class Animal:
    def say(self):
        return "This class is animal"

class Cat(Animal):
    def say(self):
        re=super().say()
        return "This animal is cat  "+re

class Dog:
    def say(self):
        print("This animal is dog")                
        
aniamls = Animal()
cat = Cat()
print(cat.say())

