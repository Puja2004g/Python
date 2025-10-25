from functools import reduce

l = [5,24,34,50,80,90,10]

def findMax(a,b):
    if(a>b):
        return a
    else:
        return b
    
print(reduce(findMax,l))