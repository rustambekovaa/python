


# month = int(input("Write the moth:"))

# def seas(found,month2):
#     for i,i2 in found.items():
#         for k,k1 in i2.items():
#             # print(k1)
#             if month2 == k:
#                 return i

# seasons = {
#     "Зима": {12: "Декабрь", 1: "Январь", 2: "Февраль"},
#     "Весна": {3: "Март", 4: "Апрель", 5: "Май"},
#     "Лето": {6: "Июнь", 7: "Июль", 8: "Август"},
#     "Осень": {9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь"}
# }
 
# print(f' Season :{seas(seasons,month)}')




bank_accounts={"Tom":{
    "balance":1000,
    "interest_rate":0.10,
    "year":5
},
    "Alisa":{
    "balance":1020,
    "interest_rate":0.10,
    "year":6
}}


 
def bank(info,name):
    for user1,item in info.items():
        if user1 == name:
            for k in range(1,item['year']+1):
               item['balance'] += item['interest_rate']*item['balance']
            return item['balance']  
name = str(input("Name:"))
result = bank(bank_accounts,name)
print(f'the end balance for user {result} som')
