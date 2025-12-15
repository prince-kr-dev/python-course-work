# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 
'''
dictionary = {
    "Seb" : "Apple",
    "Ladka" : "Boy"
}

print(dictionary["Ladka"])
'''




# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 
'''
a = set()

n1 = int(input("Enter a number : "));
a.add(n1)
n2 = int(input("Enter a number : "));
a.add(n2)
n3 = int(input("Enter a number : "));
a.add(n3)
n4 = int(input("Enter a number : "));
a.add(n4)
n5 = int(input("Enter a number : "));
a.add(n5)
n6 = int(input("Enter a number : "));
a.add(n6)
n7 = int(input("Enter a number : "));
a.add(n7)
n8 = int(input("Enter a number : "));
a.add(n8)

print(a)
'''





# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
'''
a = {18, "18"}
print(a)    #YES
'''




# 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 
'''
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20')

print(s)
print(len(s))
'''




# 5. s = {} 
# What is the type of 's'? 
'''
s = {}
print(type(s))
'''




# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 
'''
d = {}

name = input("Enter friend's name : ")
language = input("Enter language : ")
d.update({name: language})

name = input("Enter friend's name : ")
language = input("Enter language : ")
d.update({name: language})

name = input("Enter friend's name : ")
language = input("Enter language : ")
d.update({name: language})

name = input("Enter friend's name : ")
language = input("Enter language : ")
d.update({name: language})

print(d)
'''





# 7. If the names of 2 friends are same; what will happen to the program in problem 6? 

#ANSWER --->>>>>>
# The value will be updated (overwritten) for that name.
# If you enter the same name again, Python will replace the old language with the new one





# 8. If languages of two friends are same; what will happen to the program in problem 6? 

#Nothing special will happen. The program will work normally.
'''
d = {}

d["Prince"] = "Python"
d["Amit"] = "Python"   # same value, different key

print(d)
'''



# 9. Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]}
'''
Lists are mutable, and sets only allow immutable (hashable) elements. Therefore, a list cannot be included in a set, and its values cannot be changed.

✅ Correct Alternatives
✔ Use a tuple instead of list:

s = {8, 7, 12, "Harry", (1, 2)}
'''