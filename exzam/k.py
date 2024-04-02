def toCamelCase(l):
        k = ""
        for i in l:
            if i.isalpha():
                k += i
        
        print(k)
            

toCamelCase("the-stealth-warrior")