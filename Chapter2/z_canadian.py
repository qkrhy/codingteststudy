# 패스트푸드 
# 1.햄버거 , 2.사이드, 3 음료 4. 디저트 

buger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())


if buger == 1 : 
    buger = 461 
elif buger == 2 : 
    buger = 431
elif buger == 3 : 
    buger = 420
elif buger == 4 : 
    buger = 0
else : 
    print("error")

if side == 1 : 
    side = 100
elif side == 2 : 
    side = 57
elif side == 3 : 
    side = 70    
elif side == 4 : 
    side = 0
else : 
    print("error")

if drink == 1 : 
    drink = 130
elif drink == 2 : 
    drink = 160
elif drink == 3 : 
    drink = 118    
elif drink == 4 : 
    drink = 0
else : 
    print("error")

if dessert == 1 : 
    dessert = 167
elif dessert == 2 : 
    dessert = 266
elif dessert == 3 : 
    dessert = 75    
elif dessert == 4 : 
    dessert = 0
else : 
    print("error")
    
total = buger + side + drink + dessert
    
print(f"Your total Calorie count is {total}.")
