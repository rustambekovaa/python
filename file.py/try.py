# try:
#     if 2 > "str":
#         print("343")
# except TypeError as e:
#     print(f"Error: {e}")



# array=[23,3,21,10]
# try:
#     print(array[10])
# except IndexError as e:
#     print(e)



# my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
# print(my_dict['unkown'])

# try:
#     print(my_dict['unkown'])

# except Exception as e:
#     print(e)




# def example3():
#     numerator = 10
#     denominator = 0
#     try:
#         result = numerator / denominator
#     except Exception as e:
#         print(e)
# example3()



# tab_people = {
#     "Tom": {
#         "id": 1,
#         "date": 2004
#     }
# }

# user_one = tab_people.get("Tom")
# try:
#     if user_one:
#         user_one.setdefault("id", "20")
# except:
#     raise KeyError("Этот ключ уже занят")



# def open_file(file_name:str):
#     with open(file_name,"r") as file:
#         text=file.read()
#         return text

# print(open_file("text.txt"))     

# def open_file_for_add(file_name:str):
#     with open(file_name,"w+") as file:
#         text_pr=input("Goo text")
#         file.write(text_pr)
#         return text_pr
    
# print(open_file_for_add("/home/xushu/study_plan_python/start/files/task_second/text.txt"))    

# def open_file_for_append(file_name:str):
#     with open(file_name,"a") as file:
#         text_prompt=input("Goo text: ")
#         file.write(" "+text_prompt+" ")

#         return text_prompt

# print(open_file_for_append("/home/xushu/study_plan_python/start/text.txt"))
# file=open("text.txt","a")
# print("line",file=file,end='str')

# from homework_task import*

# files=["text.txt","request.txt","messages.txt"]

# files = ["text.txt", "request.txt", "messages.txt"]

# kopl=[]
# for file_name in files:
#     with open(file_name, 'r') as file:
#         content = file.read()
#         kopl.append(content)

# def to_add(file_names):
#     with open("output.txt","a") as file:
#         for i in file_names:
#             file.write(i+"\n")

# to_add(kopl)
# print(kopl)        

  
        
        
# files = ["amanai.txt", "atanai.txt", "aranai.txt"]

# kopl=[]
# for file_name in files:
#     with open(file_name, encoding='utf-8') as file:
#         content = file.read()
#         kopl.append(content)

# def to_add(file_names):
#     with open("output.txt","a") as file:
#         for i in file_names:
#             file.write(i+"\n")

# to_add(kopl)
# print(kopl)        


# import nltk
# from nltk.tokenize import sent_tokenize

# # Если это первый запуск, нужно загрузить модель для токенизации предложений
# nltk.download('punkt')

# files = ["amanai.txt", "atanai.txt", "aranai.txt"]

# kopl = []
# for file_name in files:
#     with open(file_name, encoding='utf-8') as file:
#         content = file.read()
#         sentences = sent_tokenize(content)
#         words = content.split()
#         return len(words)
#         # kopl.extend(sentences)


# def to_add(file_names):
#     with open("output.txt", "a", encoding='utf-8') as file:
#         for sentence in file_names:     
#             file.write(sentence + "\n")
            

# to_add(kopl)
# print(kopl)


  
  
import nltk
from nltk.tokenize import sent_tokenize

def akmaanai(file_path):
        with open(file_path, encoding='utf-8') as file:
            content = file.read()
            word = content.split()
            sentences = sent_tokenize(content)
            return len(sentences),len(word)
        
files = ["amanai.txt", "aranai.txt", "atanai.txt"]
with open("karina.txt", 'w', encoding='utf-8') as output:
    for file_name in files:
        sentence_count = akmaanai(file_name)
        output.write(f"Количество предложений слов в файле {file_name}: {sentence_count}\n")




# files = ['/Users/belek/Documents/programming/Backend/python/dz1.txt', '/Users/belek/Documents/programming/Backend/python/dz2.txt', '/Users/belek/Documents/programming/Backend/python/dz3.txt']

# def read(read_file:str):
#     ls = []
#     for i in read_file:
#         with open(i, 'r+') as file:
#             ls.append(file.read())
#     return ls
# gotovo = (read(files))

# def otchet(otchet_file, text):
#     with open(otchet_file, 'a') as file:
#         for i in text:
#             words = len(i.split())
#             sentences = i.count('.')
#             file.write(f"В  файле есть {words} слов и {sentences} предложений. \n")
# otchet('/Users/belek/Documents/programming/Backend/python/output.txt', gotovo)