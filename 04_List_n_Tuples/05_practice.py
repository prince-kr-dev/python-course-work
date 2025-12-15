# 1. Write a program to store seven fruits in a list entered by the user. 
'''
fruits = []
f1 = input("Enter fruit name: ")
fruits.append(f1)
f2 = input("Enter fruit name: ")
fruits.append(f2)
f3 = input("Enter fruit name: ")
fruits.append(f3)
f4 = input("Enter fruit name: ")
fruits.append(f4)
f5 = input("Enter fruit name: ")
fruits.append(f5)
f6 = input("Enter fruit name: ")
fruits.append(f6)
f7 = input("Enter fruit name: ")
fruits.append(f7)

print(fruits)
'''




# 2. Write a program to accept marks of 6 students and display them in a sorted 
# manner. 
'''
marks = []
m1 = int(input("Enter marks: "))
marks.append(m1)
m2 = int(input("Enter marks: "))
marks.append(m2)
m3 = int(input("Enter marks: "))
marks.append(m3)
m4 = int(input("Enter marks: "))
marks.append(m4)
m5 = int(input("Enter marks: "))
marks.append(m5)
m6 = int(input("Enter marks: "))
marks.append(m6)

marks.sort()
print(marks)
'''


# 3. Check that a tuple type cannot be changed in python. 
'''
a = (34,45, "Prince")

a[2] = "Kumar" #error
'''




# 4. Write a program to sum a list with 4 numbers. 
'''
l = [23,45,78,32]
print(sum(l))
'''





# 5. Write a program to count the number of zeros in the following tuple: 
# a = (7, 0, 8, 0, 0, 9) 

a = (7, 0, 8, 0, 0, 9) 
print(a.count(0))