def find(human):
    if len(human) == 0:
        print("no one likes this")
    elif len(human) ==1:
        print(f"{human[0]} likes this")
    elif len(human) == 2:
        print(f'{human[0]} and {human[1]} like this')
    elif  len(human) == 3:
        print(f"{human[0]}, {human[1]} and {human[2]} like this")
    elif len(human) >= 4:
        print( f"{human[0]}, {human[1]} and {len(human) - 2} others like this")
    
find(["Alex", "Jacob", "Mark", "Max","Mark", "Max"])