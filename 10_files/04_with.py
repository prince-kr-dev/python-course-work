f = open("10_files/file.txt")
data = f.read()
print(data)
f.close()



# this is the statement which works same as above code 

with open("10_files/file.txt") as f:
    print(f.read())