# type() : bool 
# 관계 연산자 : ==, !=, >, <, >=, <=

a3 = int(input())
a2 = int(input())
a1 = int(input())

b3= int(input())
b2 = int(input())
b1 = int(input())

apple = a1 + a2 * 2 + a3 * 3
banana = b1 + b2 * 2 + b3 * 3

if apple > banana:
    print('A')
elif apple < banana:
    print('B')
elif apple == banana:
    print('T')