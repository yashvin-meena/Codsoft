def addition(n1,n2):
    n = n1 + n2
    return n

def subtraction(n1,n2):
    n = n1 - n2
    return n

def multiplication(n1,n2):
    n = n1 * n2
    return n

def division(n1,n2):
    n = n1 / n2
    return n

choice = True
while choice:
    val1 = int(input('Enter the number:'))
    val2 = int(input('Enter the number:'))
    print('''
    1.press 1 for addtion
    2.press 2 for subtraction
    3.press 3 for multiplication
    4.press 4 for division
    ''')
    ch = int(input('Enter the choice:'))

    if ch == 1:
        result = addition(val1,val2)
    elif ch == 2:
        result = subtraction(val1,val2)
    elif ch == 3:
        result = multiplication(val1,val2)
    elif ch == 4:
        result = division(val1,val2)
    else:
        print('Invalid !!')
    print(f'Result:{result}')
    choice = input('press Y to continue:')[0]
    if choice.upper() == 'Y':
        choice = True
    else:
        choice = False