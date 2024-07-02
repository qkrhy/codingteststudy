# 반지름 r, 높이 h 인 원뿔의 부피를 계산하는 프로그램
r =  int(input())
h = int(input())

PI = 3.141592653589793 # 원주율

if 1 <= r <= 100 and 1 <= h <= 100:
    #vol = 3.14 * r * r * h / 3
    vol = PI * r ** 2 * h / 3
print(vol)

