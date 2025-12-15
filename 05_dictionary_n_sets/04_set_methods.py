"""
Python Set Methods
------------------
A set is an unordered collection of unique elements.
Sets are used when you want to store distinct values and
perform operations like union, intersection, and difference.
"""

# Create sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# add() → Adds a single element to the set
a.add(10)
print("add:", a)

# update() → Adds multiple elements to the set
a.update([20, 30])
print("update:", a)

# remove() → Removes element (raises error if not found)
a.remove(10)
print("remove:", a)

# discard() → Removes element (no error if not found)
a.discard(100)
print("discard:", a)

# pop() → Removes and returns a random element
removed = a.pop()
print("pop:", removed, a)

# clear() → Removes all elements from the set
temp = {1, 2}
temp.clear()
print("clear:", temp)

# union() → Returns all unique elements from both sets
print("union:", a.union(b))

# intersection() → Returns common elements
print("intersection:", a.intersection(b))

# difference() → Returns elements in 'a' but not in 'b'
print("difference:", a.difference(b))

# symmetric_difference() → Elements present in only one set
print("symmetric_difference:", a.symmetric_difference(b))

# intersection_update() → Keeps only common elements (updates set)
c = {1, 2, 3}
c.intersection_update({2, 3, 4})
print("intersection_update:", c)

# difference_update() → Removes common elements (updates set)
d = {1, 2, 3}
d.difference_update({2})
print("difference_update:", d)

# symmetric_difference_update() → Keeps only non-common elements
e = {1, 2, 3}
e.symmetric_difference_update({3, 4})
print("symmetric_difference_update:", e)

# isdisjoint() → Checks if no common elements exist
print("isdisjoint:", a.isdisjoint({100, 200}))

# issubset() → Checks if all elements exist in another set
print("issubset:", {1, 2}.issubset(a))

# issuperset() → Checks if set contains another set completely
print("issuperset:", a.issuperset({1, 2}))

# copy() → Returns a shallow copy of the set
f = a.copy()
print("copy:", f)
