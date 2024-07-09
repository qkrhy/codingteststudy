# https://dmoj.ca/problem/coci13c3p1

n = int(input[0])

current_word = 'A'
    
# 단어를 n번 변환
for _ in range(n):
    next_word = []
    for char in current_word:
        if char == 'A':
            next_word.append('B')
        elif char == 'B':
            next_word.append('BA')
    current_word = ''.join(next_word)

# A와 B의 개수 세기
count_A = current_word.count('A')
count_B = current_word.count('B')

print(count_A, count_B)

### 문제 풀이 실패