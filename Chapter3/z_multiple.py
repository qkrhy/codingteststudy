# https://dmoj.ca/problem/ccc11s2

tests = int(input())

# 학생 답 
student_responses = []
# 정답 
correct_answers = []

# 학생 답과 정답을 각각 리스트에 저장
for i in range(tests):
    student_responses += input()
for i in range(tests):
    correct_answers += input()

answer = 0  # 맞은 개수 초기화

# 학생 답과 정답을 비교하여 맞은 개수 세기
for i in range(tests):
    if student_responses[i] == correct_answers[i]:
        answer += 1

print(answer)