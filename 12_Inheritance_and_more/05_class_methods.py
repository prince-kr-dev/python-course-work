class Employee:
    a = 12  # Class attribute

    @classmethod
    def show(cls):
        # cls refers to the class (Employee), not the object
        print(f"The value of a = {cls.a}")


e = Employee()  # Create object
e.a = 45        # Create an INSTANCE attribute (does NOT change class attribute)

e.show()        # Calls class method
