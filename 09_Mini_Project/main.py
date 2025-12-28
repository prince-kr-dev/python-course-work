import random

# Mapping
# 1 = snake
# -1 = water
# 0 = gun

computer =  random.choice([0,-1, 1])

youStr = input("Enter your choice : (s, w, g): ")
youDict = {"s": 1, "w": -1, "g": 0}
revDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = youDict[youStr]


print(f"Computer chooses : {revDict[computer]}")
print(f"You chooses : {revDict[you]}")


if computer == you:
    print("It's a draw")

elif (computer == 1 and you == 0) or \
     (computer == -1 and you == 1) or \
     (computer == 0 and you == -1):
    print("You win!")

else:
    print("You lose!")
