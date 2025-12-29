class Employee:
    language = "Python"  #class attribute
    salary = 1200000

prince = Employee()
prince.language = "Java" #instance attribute
print(prince.name, prince.language, prince.salary)