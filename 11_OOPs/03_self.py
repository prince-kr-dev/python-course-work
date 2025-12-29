class Employee:
    language = "Python"   # Class attribute (same for all objects)
    salary = 1200000      # Class attribute

    def getInfo(self):
        # Instance method
        # "self" refers to the current object
        print(f"Language is {self.language} and salary is {self.salary}")

    # If a method does not use "self",
    # we should make it a static method
    @staticmethod
    def greet():
        # Static method
        # It does not need object data
        print("Good Morning")


prince = Employee()   # Creating an object of Employee class
# prince.language = "Java"  # This would override the class attribute for this object only


# Both method calls below are the same
prince.getInfo()          # Calling method using object
Employee.getInfo(prince) # Python internally passes the object as "self"

prince.greet()            # Calling static method
