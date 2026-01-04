# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
# present, a message without exiting the program must be printed prompting the same.
'''
try:
    with open('14_Advance_Python_1/file1.txt') as f1:
        print(f1.read())
except Exception as e:
    print(e)
try:
    with open('14_Advance_Python_1/file2.txt') as f2:
        print(f2.read())
except Exception as e:
    print(e)
try:
    with open('14_Advance_Python_1/file3.txt') as f3:
        print(f3.read())
except Exception as e:
        print(e)

print("Thank u")
'''





# 2. Write a program to print third, fifth and seventh element from a list using enumerate 
# function.
'''
l = [1,2,3,4,5,6,7,8]

for i, items in enumerate(l):
    if(i==2 or i==4 or i==6):
        print(items)
'''




# 3. Write a list comprehension to print a list which contains the multiplication table of a 
# user entered number.
'''
# Normal way
num = int(input("Enter a number : "))

table = []

for i in range(1,11):
    table.append(num * i)

print(table)

# List Comprihension
num = int(input("Enter a number : "))

table = [num * i for i in range(1,11)]

print(table)
'''






# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’.
'''
a = int(input("Enter first Number :"))
b = int(input("Enter second Number :"))

try:
    print(f"Division of a/b = {a/b}")

except ZeroDivisionError:
    print("Infinite")

print("Code executed without crash")
'''


# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

num = int(input("Enter a number : "))

table = [num * i for i in range(1,11)]

with open("14_Advance_Python_1/Table.txt", "a") as f:
    f.write(str(table) + "\n")

print(f"List of Table of {num} appended in Table.txt")
