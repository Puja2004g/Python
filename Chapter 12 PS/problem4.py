def divide(n,m):
    if(m==0):
        raise ZeroDivisionError("Infinite")
    else:
       print(n/m)

divide(1,2)
divide(2,8)
divide(0,2)
divide(2,0)