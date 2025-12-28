#Function with argument
'''
def greet(name, ending):
    print(f"Good Morning {name}")
    print(ending)

greet("Prince", "Thank you")
greet("Bob", "Thank you")
greet("Alice", "Thanks")
'''




#Function with return value
'''
def greet(name, ending):
    print(f"Good Morning {name}")
    print(ending)
    return "Done"


a = greet("Prince", "Thank you")
print(a)
'''




def avg(num1, num2, num3):
    return (num1 + num2 + num3)/3

average = avg(12,32,13)
print(average)