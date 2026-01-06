# 1. Create two virtual environments, install few packages in the first one. How do you 
# create a similar environment in the second one?
# 2. Write a program to input name, marks and phone number of a student and format it 
# using the format function like below: 
# “The name of the student is Harry, his marks are 72 and phone number is 99999888” 
'''
name = input("Enter name : ")
marks = int(input("Enter marks :"))
phone = int(input("Enter phonr n. :"))

s = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks,phone)

print(s)
'''


# 3. A list contains the multiplication table of 7. write a program to convert it to vertical 
# string of same numbers.  
'''
table = [str(7*i) for i in range(1,11)]

s = "\n".join(table)

print(s)
'''






# 4. Write a program to filter a list of numbers which are divisible by 5. 65,20,

'''
def divisible_by_5(num):
    if(num%5 == 0):
        return True
    return False

l = [12,24,65,20,76,91,35]

f = list(filter(divisible_by_5, l))

print(f)
'''



# 5. Write a program to find the maximum of the numbers in a list using the reduce 
# function. 
'''
from functools import reduce

l = [12,24,65,20,76,91,35]

def greater(a, b):
    if(a>b):
        return a
    return b


g = reduce(greater, l)

print(g)
'''
