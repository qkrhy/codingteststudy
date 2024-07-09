# https://dmoj.ca/problem/coci18c4p1

initial_wizard = input()
num_duels = int(input())

# 초기화 및 현재 마법사 설정
current_wizard = initial_wizard
wizards_obeyed = set()
wizards_obeyed.add(current_wizard)

for i in range(num_duels):
    duel = input().split()
    winner = duel[0]
    loser = duel[1]
    
    # 패배자가 현재 마법사라면 승자로 바꾸기
    if loser == current_wizard:
        current_wizard = winner
        wizards_obeyed.add(current_wizard)

print(current_wizard)
print(len(wizards_obeyed))