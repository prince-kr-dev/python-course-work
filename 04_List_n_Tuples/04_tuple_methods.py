# Creating a tuple
t = (10, 20, 30, 20, 40, 20)

print("Tuple:", t)

# 1. count() → counts occurrences of an element
print("Count of 20:", t.count(20))

# 2. index() → returns index of first occurrence
print("Index of 30:", t.index(30))

# len() → number of elements
print("Length of tuple:", len(t))

# max() → largest element
print("Maximum value:", max(t))

# min() → smallest element
print("Minimum value:", min(t))

# sum() → sum of elements
print("Sum of elements:", sum(t))

# sorted() → returns sorted list (not tuple)
print("Sorted tuple:", sorted(t))

# Tuple unpacking
a, b, c, d, e, f = t
print("Unpacked values:", a, b, c, d, e, f)