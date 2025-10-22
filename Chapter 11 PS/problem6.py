class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, vec):
        return vector(self.i + vec.i , self.j + vec.j, self.k + vec.k)
    
    def __mul__(self, vec):
        result = self.i*vec.i + self.j*vec.j + self.k*vec.k
        return result
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
v1 = vector(1,2,3)
v2 = vector(4,5,6)

print(v1+v2)
print(v1*v2)