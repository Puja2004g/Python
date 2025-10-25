l = [5,24,34,50,80,90,10]

def divisibleBy5(num):
    if(num%5==0):
        return True
    else:
        return False
    
div5 = filter(divisibleBy5, l)

print(list(div5))