# 1. Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector. 
'''
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"X = {self.x}\nY = {self.y}\n")

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"X = {self.x}\nY = {self.y}\nZ = {self.z}")


v2 = Vector2D(2,4)
v3 = Vector3D(4,3,5)

v2.show()
v3.show()
'''




# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 
'''
class Animal:
    pass

class Pets(Animal):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Dogs are barking")

d = Dog()
d.bark()
'''





# 3. Create a class ‘Employee’ and add salary and increment properties to it. 
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary. 
'''
class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # change increment based on new salary
        self.increment = ((new_salary / self.salary) - 1) * 100


e = Employee(234, 20)

print("Before setter:")
print("Salary after increment =", e.salaryAfterIncrement)
print("Increment =", e.increment)

# using setter
e.salaryAfterIncrement = 300

print("\nAfter setter:")
print("Increment =", e.increment)
print("Salary after increment =", e.salaryAfterIncrement)
'''





# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    

    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)

    def __str__(self):
        return f"{self.r} + {self.i}i"


c1 = Complex(2,4)
c2 = Complex(6,2)

print(f"Sum = {c1 + c2}")
print(f"Multiplication = {c1 * c2}")
