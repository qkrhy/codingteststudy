# https://dmoj.ca/problem/ccc18j2

n = input()

if not n.isdigit():
    exit('숫자')
    
n = int(n)
if not 1 <= n <= 100:
    exit('범위')

yesterday = input()
today = input()

occupied = 0

for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied = occupied + 1

print(occupied)