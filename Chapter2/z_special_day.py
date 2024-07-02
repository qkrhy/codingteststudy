month = int(input())
day = int(input())

    
if (0 < month < 13) and (0 < day < 32):
    if  month <= 2 and day < 18:
        print('Before')
    elif month == 2 and day == 18:
        print('Special')
    elif month ==2 and day > 18:
        print('After')
    elif month
else:
    print('Please enter again')
 