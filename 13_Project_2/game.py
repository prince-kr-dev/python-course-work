import random

print("Guess a number between 1 and 50")

generated_No = random.randint(1,50)
count = 0
while(True):
    count += 1
    enterd_Number = int(input("Guess the number : "))

    if(enterd_Number < generated_No):
        print("Higher number please")
    elif(enterd_Number > generated_No):
        print("Lower number please")
    else:
        print("You Won")
        break

print(f"You guessed {generated_No} in {count} attempts")