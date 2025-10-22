class Complex:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def __add__(self, c2):
        return Complex(self.i + c2.i, self.j + c2.j)
    
    def __mul__(self, c2):
        self.i = self.i*c2.i - self.j*c2.j
        self.j = self.i*c2.j + self.j*c2.i
        return Complex(self.i, self.j)
    
    def __str__(self):
        return f"({self.i}) + ({self.j})i"
    

    

c1 = Complex(1,2)
c2 = Complex(3,4)

print(c1+c2)

print(c1*c2)