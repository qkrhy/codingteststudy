# 입력 받기
p = int(input())
b = int(input())
d = int(input())

# 만들 수 있는 뱃지 수 계산
num = p // b

# 남은 페인트 양 계산
paint = p % b

a = num * d + paint
print(a)
