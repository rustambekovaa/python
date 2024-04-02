# admin = input("name \t")
# if admin == "admin":
#        parol = input("paroladmin \t")
#        if 8>len(parol)>4:
#            print("введите правильный пароль")
  
  
       
# name = input("name \t")
# alfa = input("alfa \t")
# count = 0 
# for i in name:
#     if i == alfa:
#         count+=1
# print(count)

  


# login = input("Login \t")
# password =input("Password  \t")
# if 8 >=len(password) >= 4:
#     if  "#" in password and "-" in password and "*" in password:
#         print("«Пароль имеет не допустимые символы #-*")
#     elif password.isdigit():
#         print("«Ваш пароль имеет только цифры исправьте»")
#     elif password.isupper() or password.islower():
#         print("Ваш пароль не безопасный ")
#     else:
#         print("вы зарегистрированы")



# pas = "akmaanai"
# login = input("Login\t")
# c = 5
# while c>0:
#     password = input("password")
#     if password != pas:
#         c-=1
#         print(f"u vas ostalos {c} popytok")
#     else:
#         print("вы зарегистрированы")
#         break
   
   
   
# n= int(input("sifra"))   
# s= int(input("stepen"))
# k=1
# for i in range(1,n+1,1):
#    k=s**i
# print(k)
    
    
    
# k = [1,2,3,4,5,7,10]
# a=0
# while a < len(k):
#     print(k[a])
#     a+=1
  
  
  
# k = [1,2,3,4,5,7,10]
# a=0
# for i in k:
#     a+=i
# print(a)


# k = [1,2,3,4,5,7,10,20]
# a=0
# k1=0
# while a < len(k):
#     k1+= k[a]
#     a+=1
# print(k1)



# k = int(input())
# l = int(input())
# for i in range(k,l+1):
#     print(i,end=' ')

# 1) Есть массив с некоторыми числами. Все числа равны, кроме одного. Попробуйте найти его!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0,55, 0, 0 ]) == 0,55
# Гарантируется, что массив содержит не менее 3 чисел.


# number = [ 1, 1, 1, 2, 1, 1 ]
# k =""
# for i in number:
#     for j in i:
#         if i != j:
#             k = j
#             print(k)


# numbers = [ 0, 0, 0,55, 0, 0]
# k = 0 
# for i in numbers:
#     if numbers.count(i) == 1:
#         k = i
#         break
# print(k) 



# k=[1,6,7,9,2,4,3,8,4,1]
# k.sort(reverse=False)
# print(k)

# Search the max number 


# k = [3,4,6,10,2,7,8,123]
# k1 = 0
# for i in k:
#     if i > k1:
#         k1=i
# print(k1)   

# k = [3,4,6,10,2,7,8]
# k1 = 0
# for i in k:
#     if i > k1:
#         k1=i
# print(k.index(k1))   


# k = [3,4,6,10,2,7,8,123]
# k1 = k[0]
# for i in k:
#     if i<k1: 
#         k1 = i
# print(k1)


# l = [1,2,3,4,-2,6,-4,6,-4]
# lm =[]
# for i in l:
#     if i<0:
#         lm.append(i)
#         l.remove(i)
# print(l)
# print(lm)  


# k = [-21,-1,1,31,-7,0]
# k2 = []
# for i in k:
#     if i<0:
#         i = i**2
#         k2.append(i)
#     elif i >0:
#         i = i**3
#         k2.append(i)
# print(k2)



# Фильтрация четных чисел:
# Создайте список четных чисел от 0 до 20 с использованием list comprehension.

# numbers = [1, 2, 3, -4, 5, 6, -7, 8, 9, 10]
# k = [x for x in numbers if x > 0]
# print(k)

# Генерация списка квадратов положительных чисел:
# Создайте список квадратов чисел от 1 до 10, но исключите нули и отрицательные числа.

# numbers = [1, 2, 3, -4, 5, 6, -7, 8, 9, 10]
# k = [x**2 for x in numbers if x > 0]
# print(k)

# Преобразование слов в список их первых букв:
# У вас есть список слов. Создайте новый список, содержащий первые буквы каждого слова. Например, если у вас есть ['apple', 'banana', 'cherry'], результат должен быть ['a', 'b', 'c'].

# alfa=['apple', 'banana', 'cherry']
# k = [x[0] for x in alfa ]
# print(k)

# Фильтрация слов по длине:
# У вас есть список слов. Создайте новый список, содержащий только те слова, длина которых больше 5 символов. Например, если у вас есть ['apple', 'banana', 'cherry'], результат должен быть ['banana', 'cherry'].

# leng = ['apple', 'banana', 'cherry']
# k1 = [ k for k in leng if len(k)  > 5] 
# print(k1)

# Генерация списка всех троек чисел в диапазоне от 1 до 5:
# Создайте список всех возможных троек (a, b, c), где a, b и c - числа от 1 до 5.

# numbers = range(1, 6)
# all_triplets = [(a, b, c) for a in numbers for b in numbers for c in numbers]
# print(all_triplets)

# Создание списка квадратов чисел от 1 до 10, пропуская числа, которые кратны 3:
# Создайте список квадратов чисел от 1 до 10, но пропустите числа, которые кратны 3.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = [x for x in numbers if x%3==0]
# print(k)



# Деструктуризация в циклах

# tuples_list = [(1, 2), (3, 4), (5, 6)]

# sum_of_second_elements = 0

# for tuple_item in tuples_list:
#     sum_of_second_elements += tuple_item[1]

# print(sum_of_second_elements)

employs2 = dict() 
name = input("name \t")
age = input("age \t")
number = input("number \t")
employs2[name] = {"age":age,"number":number}    
print(employs2)



