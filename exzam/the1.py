# find_uniq = [ 1, 1, 1, 2, 1, 1 ]
# find_uniq = [ 0, 0, 0,55, 0, 0 ]
# find_uniq = [ 2,3,3,3,3,3,3,3,3 ]


# k = find_uniq[0]
# for i in find_uniq:
#     if i != k :
#         print(f"уникальный номер {i}")
#     elif i==k:




find_uniq = [ 2,3,3,3,3,3,3,3,3 ]

for num in find_uniq:
    if find_uniq.count(num) == 1:
        print(num)



