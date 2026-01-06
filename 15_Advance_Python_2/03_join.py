# join() is a STRING method
# It is used to combine elements of an iterable into a single string
# IMPORTANT: All elements inside the iterable must be strings



# List of names that we want to combine into a single string
a = ["Prince", "Rohan", "Sonu"]

# Join all list elements using '-' as a separator
# Result will be a single string where names are separated by hyphens
final_1 = "-".join(a)

# Join all list elements using '::' as a separator
# Useful when a clearer or more unique separator is required
final_2 = "::".join(a)

# Join all list elements using '%' as a separator
# Demonstrates that any string can be used as a separator
final_3 = "%".join(a)

# Printing the final joined strings
print(final_1)
print(final_2)
print(final_3)
