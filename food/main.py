# from datetime import datetime
# import time
# def iterator():
#     count=0
#     def generator():
#         nonlocal count
#         count+=1  
        
#         return count

#     return generator


# def decorator(func):
#     def wraper(sdf):
#         print("start function",datetime.now())
#         print(func(sdf))
#         print("end function",time.sleep(3),datetime.now())
#     return wraper    


# @decorator    
# def string_func(text):
#     return text    

# string_func("trttr")
# # print(a.__name__)



dict1 = {
    "Belek": {"role":"admin"},
    "Samagan": {"role":"manager"}
    }


def role_required(role):
    def decarotor(func):
        def wraper(username):
            user=dict1.get(username)
            role_user=user.get('role')
            if role_user==role:
                func(username)
            else:
                print("This user is dont has permisiion")

        return wraper
    return decarotor                
                



@role_required("admin")
def is_admin(usernam):
    print("Этот пользователь являтся админом",usernam)

@role_required("manager")
def is_manager(username):
    print("is manager",username)

# @role_required("user")
def user_(username):
    print("Этот ползовател обычный")        
