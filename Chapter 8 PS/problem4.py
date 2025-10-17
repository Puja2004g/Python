def recursionSum(n):
    if n == 0:
        return 0
    else:
        return n + recursionSum(n - 1)

    
n = int(input("Enter a number: "))

# Call the function
result = recursionSum(n)

print(f"Sum of first {n} natural numbers is: {result}")