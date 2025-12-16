# 1. Write a program to find the greatest of four numbers entered by the user. 
'''
a = int(input("Enter 1st no. : "))
b = int(input("Enter 2nd no. : "))
c = int(input("Enter 3rd no. : "))
d = int(input("Enter 4th no. : "))

if(a > b and a>c and a>d):
    print(f"{a} is greater")

elif(b>a and b>c and b>d):
    print(f"{b} is greater")

elif(c>a and c>b and c>d):
    print(f"{c} is greater")

else:
    print(f"{d} is greater")
'''


# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.
'''
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

total_percentage = (sub1 + sub2 + sub3) / 3

if (sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and total_percentage >= 40):
    print("Student has PASSED")
else:
    print("Student has FAILED")
'''





# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.
'''
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter the comment : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is spam")

else:
    print("This comment is not a spam")
'''




# 4. Write a program to find whether a given username contains less than 10 characters or not. 
'''
username = input("Enter usrname :")

if(len(username) < 10):
    print("Less than 10 characters")

elif(len(username) == 10):
    print("Length is equal to 10")

else:
    print("Greater than 10 characters")
'''


# 5. Write a program which finds out whether a given name is present in a list or not.
'''
l = ["Prince", "Aman", "Rohan", "Sohan"]

name = input("Enter name : ")

if(name in l):
    print("Name is in list")
else:
    print("Name is not in list")
'''




# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F 

'''
marks = int(input("Enter marks : "))

if(marks >= 90 and marks <=100):
    grade = "Ex"

elif(marks >= 80 and marks < 90):
    grade = "A"

elif(marks >= 70 and marks < 80):
    grade = "B"

elif(marks >= 60 and marks < 70):
    grade = "C"

elif(marks >= 50 and marks < 60):
    grade = "D"

elif(marks < 50):
    grade = "F"

print(grade)
'''




# 7. Write a program to find out whether a given post is talking about "Prince" or not. 

post = "Hey my name is prince , prince is computer science student"

if("Prince".lower() in post.lower()):
    print("Post is talking about Prince")

else:
    print("Post is not talking about Prince")