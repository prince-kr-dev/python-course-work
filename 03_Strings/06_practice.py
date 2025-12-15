# 1. Write a python program to display a user entered name followed by Good 
# Afternoon using input () function.
'''
name = input("Enter your name: ")
print(f"Good afternoon {name}")
'''



# 2. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# ''' 


# Solution................................
# letter = '''Dear <|Name|>, 
# You are selected! 
# <|Date|>'''

# print(letter.replace("<|Name|>", "Prince").replace("<|Date|>","12/13/2025"))




# 3. Write a program to detect double space in a string. 
'''
str = "Prince kumar, MERN  Stack developer"
print(str.find("  "))
'''





# 4. Replace the double space from problem 3 with single spaces.
'''
str = "Prince kumar, MERN  Stack developer"
print(str.replace("  ", " "))
'''







# 5. Write a program to format the following letter using escape sequence 
# characters. 
# letter = "Dear Harry, this python course is nice. Thanks!"

letter = "Dear Harry, \n\tthis python course is nice. \nThanks!"
print(letter)