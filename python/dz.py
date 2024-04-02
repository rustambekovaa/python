# array=[1,2,'a','b']
# k = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# for i in array:
#     # print(i)
#     for l in k:
#         if l == i:
#             array.remove(i)
#     print(array)
        
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# difference_set = set1.difference(set2)
# # или
# difference_set = set1 - set2
# print(difference_set)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# intersection_set = set1.intersection(set2)
# # или
# intersection_set = set1 & set2
# print(intersection_set)



#  a = int(input("Введите число  ")) 
# b = str(a) 
# string = "" 
# for i in b: 
#     d = int(i) ** 2 
#     string += str(d) 
# print(string)


# text = input("Введите что-то:")
# k = ''
# k1=''
# k3=''
# for i in text:
#     if i.islower():
#         k+=i
#         del i
# for i2 in k:
#     if i2 in k1:
#         k3+=")"
#     elif i2 not in k1:
#         k3+="("
# print(k3)


# def k(a):
#     k0 = 0
#     for i in a:
#         k0+=i
#     return k0
# k1 = [1,2,34,5,]
# print(k(k1))


# def k(a):
#     k0 = a[0]
#     for i in a:
#         if i is not type(bool) and i is not type(str):
#             if i > k0:
#                 k0 = i
#     return k0
# k1 = [1,2,34,5,"sddsd",True]
# print(k(k1))

# def k(a):
#     k0 = a[0]
#     for i in a:
#         if not isinstance(i, (bool, str)):
#             if i > k0:
#                 k0 = i
#     return k0

# k1 = [1, 2, 34, 5, "sddsd", True]
# print(k(k1))


# def k(a):
#     l =0
#     for i in a:
#         if i %2 == 0:
#           l+=1  
#     return l
# k1 = [1, 2, 34, 5,10,20,40]
# print(k(k1))


# def k(a,b):
#     t = [*a,*b] 
#     return t
# k1 = [1, 2, 3]
# k2 = [4,5,6]
# print(k(k1,k2))


# def k(a):
#     massiv = []
#     l =" "
#     for i in a:
#         massiv.append(i)
#     massiv.reverse()
#     for i2 in massiv:
#         l += " ".join(i2)
#     # l+= str(massiv)
#     return l
# k1 ="belek"
# print(k(k1))


# def k(a):
#    a1 = a[::-1]
#    return a1
# k1 ="belek"
# print(k(k1))



# def k(a):
#    a1 = a[::-1]
#    if a1 == a:
#     return True
#    else:
#        return False
# k1 ="121"
# print(k(k1))
 

# def k(a):
#    a1 = " ".join(reversed(a))
#    if a1 == a:
#     return True
#    else:
#        return False
# k1 ="lol"
# print(k(k1))



# def k(a):
#     k2 = set()
#     for i in a:
#         k2.add(i)
#     return k2
# k1 = (1, 2,3,4,5,4)
# print(k(k1))


# def k(a): 
#     count = 0
#     alfa = "ayuoie"
#     for i in a:
#         for i2 in alfa:
#             if i == i2:
#                 count +=1
#     return count
# k1 ="asdfghuoaaaa"
# print(k(k1))


# напишем функцию которая проверяет наш пароль Длина пароля должна быть не менее 8 символов.
# Пароль должен содержать как минимум одну заглавную букву.
# Пароль должен содержать как минимум одну строчную букву.
# Пароль должен содержать как минимум одну цифру.
# Пароль должен содержать как минимум один специальный символ (например, !, @, #, $, %).если все эти условии верны то функция возвращает True иначе false

# password = input('Введите пароль')
# def text(a):
#     sym = ('!@#$%')
#     numer = ("1234567890")
#     for i in a:
#         for i2 in sym:
#             for i3 in numer:
#                 if len(a) >= 8 and i.isupper() and i.lower() and i == i2 and i == i3:
#                     return 1
              
# print(text(password))



# def k(password):
#     return (
#         len(password) >= 8 and
#         any(char.isupper() for char in password) and
#         any(char.islower() for char in password) and
#         any(char.isdigit() for char in password) and
#         any(char in '!@#$%' for char in password)
#     )

# k1 = input("Введите пароль: ")
# if k(k1):
#     print(True)
# else:
#     print(False)




# def k(a):
#     # return a.keys(), a.values()4
#     return a.items()
    
# k1 = {
#     'Akmaanai': '19',
#     'Atanai': '18',
#     'Akanai': '17'
# }

# print(k(k1))



#Фоктариал+ 


# number = int(input("Введите цифру:"))
# def k(a):
#     l = 1
#     for i in range(1,a+1):
#         l = l * i
#     return l
# print(k(number))ь 


# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000


 