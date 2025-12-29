# 1. Create a class “Programmer” for storing information of few programmers 
# working at Microsoft. 
'''
class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
    
    def getInfo(self):
        print(f"Name = {self.name}\nCompany = {self.company}\nSalary = {self.salary}\nPincode = {self.pincode}")


employee = Programmer("Prince", 1300000, 841228)
employee.getInfo()
print()
employee = Programmer("Aman", 3000000, 841262)
employee.getInfo()
print()
employee = Programmer("Rohan", 2300000, 841285)
employee.getInfo()
'''



# 2. Write a class “Calculator” capable of finding square, cube and square root of a 
# number. 
'''
import math

class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"Square = {self.n * self.n}")

    def cube(self):
        print(f"Cube = {self.n * self.n * self.n}")

    def root(self):
        print(f"Square Root = {math.sqrt(self.n)}")



a = Calculator(4)
a.square()
a.cube()
a.root()
'''



# 3. Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute? 
'''
class Person:
    a = 12 #class attribute

val = Person()
val.a = 0 #instance attriibute

print(val.a)
print(Person.a)

# No, it does NOT change the class attribute.
'''





# 4. Add a static method in problem 2, to greet the user with hello.
'''
import math

class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"Square = {self.n * self.n}")

    def cube(self):
        print(f"Cube = {self.n * self.n * self.n}")

    def root(self):
        print(f"Square Root = {math.sqrt(self.n)}")

    @staticmethod
    def greet():
        print("Hello, Good Morning")



a = Calculator(4)
a.square()
a.cube()
a.root()
a.greet()
'''





# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 
'''
from random import randint

class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def bookTkt(self, fromm, to):
        print(f"Ticket is booked in train No. {self.trainNo} from {fromm} to {to}")

    def getStatus(self):
        print(f"Train {self.trainNo} is running on time")

    def getFare(self, fromm, to):
        print(f"Ticket fare in train No. {self.trainNo} from {fromm} to {to} = {randint(222,777)}")


t = Train(12984)
t.bookTkt("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi","Mumbai")

'''




# 6. Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf”  and see the effects. 

class Person:
    def __init__(slf, name):
        slf.name = name

    def show(slf):
        print("Name is:", slf.name)

p1 = Person("Prince")
p1.show()


#It does not change anything. The output is the same with self or slf, but it is not good programming practice.