bowl1 = int(input())
bowl2 = int(input())
bowl3 = int(input())

# sort 함수 사용 
#bowls = [bowl1, bowl2, bowl3]
#bowls.sort()
#bowl = bowls[1]
#print(bowl)

if (bowl2 <= bowl1 and bowl1 <= bowl3) or (bowl3 <= bowl1 and bowl1 <= bowl2):
    bowls = bowl1
elif (bowl1 <= bowl2 and bowl2 <= bowl3) or (bowl3 <= bowl2 and bowl2 <= bowl1):
    bowls = bowl2
else:
    bowls = bowl3
    
print(bowls)