class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        if self.salary < 5000:
            self.increment = self.salary*0.10
        
        else :
            self.increment = self.salary*0.05

# Create an Employee object
emp = Employee(4000, 0)

# Call the setter to update increment based on salary
emp.salaryAfterIncrement = None  # We just trigger the setter

# Check the results
print("Salary:", emp.salary)
print("Increment:", emp.increment)
print("Salary after increment:", emp.salaryAfterIncrement)
