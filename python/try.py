try:
    a=float(input('Enter number 1:'))
    sign=input('Enter sign:')
    b=float(input('Enter number 2:'))

    if sign=='+':
        print(a+b)
    elif sign=='-':
        print(a-b)
    elif sign=='*':
        print(a*b)
    elif sign=='/':
        print(a/b)
    elif sign=='^':
        print(a**b)
except ValueError :
    print('not recignizition')
