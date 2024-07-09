# https://dmoj.ca/problem/wc17c3j3

# 유효 Valid, 유효하지 않은 Invalid
password = input()

#소문자 Lower, 대문자 Upper, 숫자 Digit
lower_count = sum(1 for char in password if char.islower())
upper_count = sum(1 for char in password if char.isupper())
digit_count = sum(1 for char in password if char.isdigit())

if len(password) >= 6 and len(password) <= 20:
    if lower_count >= 3 and upper_count >= 2 and digit_count >= 1:
        print("Valid")
    
    print("Invalid")