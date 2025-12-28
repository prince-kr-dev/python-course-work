# 1. Write a program using functions to find greatest of three numbers.
'''
def greatest(n1, n2, n3):
    if(n1 > n2 and n1 > n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    elif(n3>n1 and n3>n2):
        return n3
    
g = greatest(23,54,12)
print(f"Greatest among all numbers is : {g}")
'''




# 2. Write a python program using function to convert Celsius to Fahrenheit.
'''
def C_to_F(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

degC = int(input("Enter the celsius : "))
f = C_to_F(degC)
print(f"{degC} Celsius = {f} Farhenheit")
'''




# 3. How do you prevent a python print() function to print a new line at the end.
'''
print("Hello ", end="")
print("World")
'''






# 4. Write a recursive function to calculate the sum of first n natural numbers.

def sumOfFirstN_natural(n):
    if(n == 1):
        return 1
    return n + sumOfFirstN_natural(n-1)


n = int(input("ENter the number : "))
s = sumOfFirstN_natural(n)
print(f"Sum o dfirst {n} numbers = {s}")




# 5. Write a python function to print first n lines of the following pattern: 
# *** 
# **               - for n = 3 
# * 
 
# 6. Write a python function which converts inches to cms. 
# 7. Write a python function to remove a given word from a list ad strip it at the same 
# time. 
# 8. Write a python function to print multiplication table of a given number. 
  
