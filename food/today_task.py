# def calucator():
#     k = []
    
#     # k3 = 0
#     def countr(a):
#         k.append(a)
#         k3 = sum(k) / len(k)
#         return k3 
#     return countr
    
    
# a=calucator()
# print(a(10))
# print(a(10))
# print(a(30))
    
import time
    
def retry(max_attemps,interval):
    def decorator(func):
        def wrapper(args):
            k = 0
            while k<max_attemps:
                try:
                    func(args)
                    print(args)
                    return 
                except Exception as e:
                    k+=1
                    print(e)
                    time.sleep(interval)
        return wrapper
    return decorator       

@retry(max_attemps=3,interval=3)
def add(x):
    return x/0
add(9)