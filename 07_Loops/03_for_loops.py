# This loop prints numbers from 0 to 4 (total 5 numbers)
print("Printing numbers from 0 to 4:")

for i in range(5):
    print(i)


# This loop prints numbers from 0 to 96, increasing by 4 each time
print("\nPrinting numbers from 0 to 96 with a step of 4:")

for i in range(0, 100, 4):
    print(i)


# Tuple iteration: prints all elements of the tuple
t = (12, 34, 56, 7, "Prince")
print("\nPrinting elements of the tuple:")

for i in t:
    print(i)


# List iteration: prints all elements of the list
l = [23, 45, 68, 32, 45, 67798, 89]
print("\nPrinting elements of the list:")

for i in l:
    print(i)



# String iteration: prints each character of the string
s = "Prince"
print("\nPrinting each character of the string:")

for ch in s:
    print(ch)