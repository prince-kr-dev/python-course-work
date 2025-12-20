# 1. Write a program to print multiplication table of a given number using for loop. 
'''
n = int(input("Enter a number : "))

for i in range(1,11):
    print(f"{n} x {i} = {n * i}")
'''




# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 
# l = ["Harry", "Soham", "Sachin", "Rahul"] 
'''
l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name[0] == "S"):
        print(name)
'''




# 3. Attempt problem 1 using while loop. 
'''
n = int(input("Enter a number : "))

i = 1
while(i < 11):
    print(f"{n} x {i} = {n * i}")
    i += 1
'''





# 4. Write a program to find whether a given number is prime or not. 
'''
n = int(input("Enter a number : "))

for i in range(2 , n):
    if((n % i) == 0):
        print("Number is not prime")
        break
else:
    print("Number is prime")
'''



# 5. Write a program to find the sum of first n natural numbers using while loop.
'''
n = int(input("Enter the number : "))

sum = 0

i = 1

while(i <= n):
    sum += i
    i+=1

print(sum)
'''





# 6. Write a program to calculate the factorial of a given number using for loop. 
'''
n = int(input("Enter the number : "))

fact = 1

for i in range(1,n+1):
    fact *= i

print(fact)
'''





# 7. Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3 
'''
n = int(input("Enter the number : "))

for i in range(1, n+1):
    # Print spaces
    print(" " * (n - i), end="")
    # Print stars
    print("*" * (2*i - 1))
'''







# 8. Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 
'''
n = int(input("Enter the number : "))

for i in range(1, n+1):
    print("*" * i)
'''




# 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * * 
'''
n = int(input("Enter the number : "))

for i in range(1, n+1):
    for j in range(1, n+1):
        if(i == 1 or i == n or j == 1 or j == n):
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''



# 10. Write a program to print multiplication table of n using for loops in reversed 
# order.

n = int(input("Enter the number : "))

for i in range(1, 11):
    print(f"{n} x {11-i} = {n * (11-i)}")
