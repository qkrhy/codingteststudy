# 피자의 넓이 1 ~ 3
#치즈 비율 0 ~ 100 

width = int(input())
cheesins = int(input())

if width == 1 and cheesins <= 50:
    pizza = ('fairly')

elif width == 3 and cheesins >= 95:
    pizza = ('absolutely')

else:
    pizza = ('very')

print(f'C.C. is {pizza} satisfied with her pizza.')