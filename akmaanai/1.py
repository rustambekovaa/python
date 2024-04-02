# def say_hello():
#     print('Hello world!')


# say_hello()

# var = say_hello

# # var()


# def sum(a, b, c=1, *args, **kwargs):
#     print(len(kwargs))
#     print(args)
#     return a + b + c

# nums = [12, 12, 43,324, 324, 234, 23, 42, 3423423, 32423, 4234]

# res = sum(*nums, e=1, d=1)

# print(res)









# def is_even(num):
#     return num % 2 == 0

# is_even2 = lambda num: num % 2 == 0

# res = is_even(13)
# res2 = is_even2(12)

# print(res, res2)








# name = 'python is the most popular pr language'


# def concat(val, start=0, end=None, step=1):
#     res = ''
#     if end is None:
#         end = len(val)
#     for i in range(start, end, step):
#         res += val[i]

#     return res


# print(name[0:: 2])
# print(concat(name, 0, 6))







# staff = {
#     'name': 'Badalov Nurullo',
#     'age': 20,
#     'experience': 1
# }

# name = staff['name']
# staff['height'] = 168
# staff.setdefault('role', 'tester')
# staff['weight'] = 67

# print(staff.get('weight', 78))
# print('Staff as dict:', staff)

# print(list(staff.values()))

# staff.update({'salary': 15000})

# print('\nStaff values:')
# for val in staff.values():
#     print(val)

# print('\nStaff keys:')
# for key in staff.keys():
#     print(key)


# res = staff.pop('salary', 60000)

# print(f'res: {res}')


# print('\nStaff keys and vals:')
# for key, val in staff.items():
#     print(f'{key}: {val}')







# nums = [i for i in range(10) if i != 4]

# num = 4 if 4 in nums else 3 if 3 in nums else 0

# print(nums)
# print(num)





# USER = 'admin'
# PASSWORD = 'qwerty'

# username = input('Enter username: ')
# password = input('Enter password: ')
 
# is_authenticated = USER == username and password == PASSWORD


# def _is_authenticated(func):
#     def inner_func(*args):
#         if is_authenticated:
#             func(*args)
#         else:
#             print('The user must be authenticated')

#     return inner_func


# @_is_authenticated
# def say_hello(name=USER):
#     print(f'{name}, Hello World!')


# @_is_authenticated
# def say_goodbye():
#     print('Good bye World!')


# say_hello('Akmaanai')