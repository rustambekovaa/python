def power(k1,k2):
    # k0 = 0 
    if k2 == 0:
        return 1
    else: 
        k3 = k1*power(k1,k2-1)
        return k3
print(power(2,5))


# ///////////////////////////

def deviderx(x):
    def devidery(y):
        return y/x
    return devidery

# res = deviderx(2)
res = deviderx(3)

# print(res(10))
print(res(9))

# //////////////////////////



# import logging
# logging.basicConfig(level = logging.DEBUG)
# def decor(func):
#     def wrapper(*args):
#         result =  func(*args)
#         logging.info(f'  Резултать: {result}')
#         return result
#     return wrapper 



# @decor
# def add(a,b):
#     return a+b 
# add(3,5)
# logging.debug( u'This is a debug message' )
# logging.info( u'This is an info message' )
# logging.warning( u'This is a warning' )
# logging.error( u'This is an error message' )
# logging.critical( u'FATAL!!!' )   