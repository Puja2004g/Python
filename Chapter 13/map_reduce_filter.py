from functools import reduce

# map 
l = [2,3,4,5,6]

square = lambda x:x*x

sqlist = map(square, l)
print(list(sqlist))

# filter
def even(n):
    if(n%2==0):
        return True
    else:
        return False
    
filList = filter(even,l)
print(list(filList))

# reduce
def sum(a,b):
    return a+b

print(reduce(sum,l))