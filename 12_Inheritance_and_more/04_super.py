# Base (parent) class
class Employee:
    def __init__(self):
        # This constructor runs when an Employee object is created
        print("Constructor of Employee")

    a = 1  # Class attribute of Employee


# Child class inheriting from Employee
class Programmer(Employee):
    def __init__(self):
        # Calls the constructor of Employee
        super().__init__()
        print("Constructor of Programmer")

    b = 2  # Class attribute of Programmer


# Child class inheriting from Programmer (multilevel inheritance)
class Manager(Programmer):
    def __init__(self):
        # Calls the constructor of Programmer (and Employee via super)
        super().__init__()
        print("Constructor of Manager")

    c = 3  # Class attribute of Manager



# p = Employee()
# print(p.a)

# q = Programmer()
# print(q.a, q.b)

# Creating object of Manager class
r = Manager()

# Accessing class attributes inherited from all parent classes
print(r.a, r.b, r.c)
