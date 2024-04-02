# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000



dict = {
    '':100,
    "D": 500,
    "C" : 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I":  1   
}

number = input("Write the date: ").upper()

count = 0
for i in dict:
    for j in number:
        if i == j:
            count+= dict[i]
print(count)
 
   

