"""
Python Dictionary Methods
-------------------------
A dictionary stores data in key-value pairs.
Keys must be unique, and values can be of any type.
Dictionaries are used to represent structured data.
"""

# Create dictionary
student = {
    "name": "Prince",
    "age": 22,
    "course": "MERN"
}

# get() → Returns value for key (no error if key not found)
print("get:", student.get("name"))

# keys() → Returns all keys
print("keys:", student.keys())

# values() → Returns all values
print("values:", student.values())

# items() → Returns key-value pairs
print("items:", student.items())

# update() → Adds or updates key-value pairs
student.update({"age": 23, "city": "Delhi"})
print("update:", student)

# setdefault() → Returns value, sets default if key not found
student.setdefault("country", "India")
print("setdefault:", student)

# pop() → Removes item with given key
student.pop("city")
print("pop:", student)

# popitem() → Removes last inserted item
student.popitem()
print("popitem:", student)

# del → Deletes item using key
del student["course"]
print("del:", student)

# copy() → Creates a shallow copy
student_copy = student.copy()
print("copy:", student_copy)

# clear() → Removes all items
student.clear()
print("clear:", student)

# fromkeys() → Creates dictionary from keys with same value
keys = ["id", "email", "phone"]
default_dict = dict.fromkeys(keys, None)
print("fromkeys:", default_dict)
