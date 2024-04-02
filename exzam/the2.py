
# oroz -> ()()
# ORoz -> ]]))
# OrOz -> [)[)



a = input("Введите что-то чтобы он шифровался ")
b = str(a)

result = ""
for i in b:
    if i.islower() and b.count(i) > 1:
        result += "("
    elif i.islower() and b.count(i) ==1 :
        result += ")"
    if i.isupper() and b.count(i) > 1:
        result += "["
    elif i.isupper() and b.count(i) ==1 :
        result += "]"
   
print(result)

