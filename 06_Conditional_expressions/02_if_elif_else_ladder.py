a = int(input("Enter your age : "))

if(a >= 18):
    print("You can vote")
    
elif(a < 0):
    print("You are entering invalid age")

elif(a == 0):
    print("You entered 0")

else:
    print("You can't vote")


print("End of program")