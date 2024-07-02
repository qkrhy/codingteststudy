str = str(input())

# count 
happy = str.count(':-)')
sad = str.count(':-(')

if happy == 0 and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif sad > happy:
    print('sad')
elif sad == happy:
    print('unsure')
    
    