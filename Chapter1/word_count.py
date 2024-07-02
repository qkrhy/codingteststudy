a = input()
length = len(a)

if length == 0 or length > 80:
    exit("길이")
if a[0] == ' ' or a[-1] == ' ':
    exit("공백")
    
#num = len(a.split(' '))
# count() 함수를 사용하여 공백의 개수를 세어서 단어의 개수를 구함
num = a.count(' ') + 1
print(num)