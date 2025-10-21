class Calulator:
    @staticmethod
    def greet():
        print("Hello")

    def square(num):
        return num*num
    
    def cube(num):
        return num*num*num
    
    def square_Root(num):
        return num**(1/2)
    

sq = Calulator.square(2)
cu = Calulator.cube(2)
root = Calulator.square_Root(4)
print(sq)
print(cu)
print(root)