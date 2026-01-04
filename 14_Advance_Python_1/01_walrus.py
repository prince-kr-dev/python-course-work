#without walrus operator
'''
num = int(input("Enter a number: "))
while num > 0:
    print(num)
    num = int(input("Enter a number: "))
'''


#with walrus operator
'''
while (num := int(input("Enter a number: "))) > 0:
    print(num)
'''


'''
while (name := input("Enter name: ")) != "":
    print("Hello", name)
'''


if((num := int(input("Enter a number :"))) == (num2 := int(input("Enter 2nd number :")))):
    print("Numbers are equal")
else:
    print("Numbersis are not equal")