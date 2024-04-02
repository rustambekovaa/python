import random
number = random.randint(1, 10)
print(number)
k = 4
while k>0:
    number1 = int(input("Введите цифру от 1 до 10 "))
    if number1 == number:
        print("WINNER")
        break
    else:
        print(f"You have live:{k}")
    k -=1
        
    