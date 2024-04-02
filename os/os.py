# create folder
# import os
# os.mkdir("C:\Users\user\Desktop\python1\os.py")



# #has is file ?
# x=os.path.exists("/home/xushu/study_plan_python/start/while/models")
# print(x)

import os

folder = input("Напиши называние файла: ")
x=os.path.exists(folder)
if x:
    print("ERRO")
else:
    os.mkdir(folder)
    def to_add(name):
        with open(os.path.join(folder, "output.txt"),'w',encoding='utf-8') as file:
            file.write("dfghjkl;")
to_add(folder)
    
    


