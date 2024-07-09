# https://dmoj.ca/problem/coci18c3p1

word = input()  # 단어 입력받기

total = 0 
sequence = ['H', 'O', 'N', 'I']  
current_index = 0  

# 입력받은 단어의 각 문자에 대해 반복
for char in word:
    # 현재 문자가 sequence의 current_index 위치에 있는 문자와 일치하는 경우
    if char == sequence[current_index]:
        current_index += 1  
        
        if current_index == 4:
            total += 1 
            current_index = 0  

print(total)