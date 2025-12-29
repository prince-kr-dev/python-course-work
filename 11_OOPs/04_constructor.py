class Employee:
    language = "Python"  #class attribute
    salary = 1200000

    #dunder method which called automatically when object is created
    def __init__(self, name, language, salary):  
        print("I am creating an object")
        self.name = name
        self.salary = salary
        self.language = language



    def getInfo(self):
        print(f"Name = {self.name}\nLanguage = {self.language}\nSalary = {self.salary}")


    @staticmethod
    def greet():
        print("Good Morning")  


prince = Employee("Prince", "Java", 1500000)
prince.getInfo()
prince.greet()