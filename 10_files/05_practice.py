# 1. Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 
'''
f = open("10_files/poem.txt")
content = f.read()
if("Twinkle" in content):
    print("Twinkle word present in the poem file")
else:
    print("Twinkle word not present in the poem file")

f.close()
'''





# 2. The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi-
# score whenever the game() function breaks the Hi-score. 
'''
import random

def game():
    print("You are playing a game :")
    score = random.randint(1, 60)
    print(f"Your score : {score}")
    return score

score = game()


with open("10_files/hi-score.txt", "r") as f:
    hiscore = f.read()
    if hiscore == "":
        hiscore = 0
    else:
        hiscore = int(hiscore)

if score > hiscore:
    with open("10_files/hi-score.txt", "w") as f:
        f.write(str(score))
'''




# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old. 
'''
def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"10_files/Tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)
'''



# 4. A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file. 
'''
with open("10_files/Donkey.txt") as f:
    content = f.read()

updatedContent = content.replace("Donkey", "######")

with open("10_files/Donkey.txt", "w") as f:
    content = f.write(updatedContent)
'''





# 5. Repeat program 4 for a list of such words to be censored. 
'''
words = ["makes", "perfect"]

with open("10_files/for_fifth.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("10_files/for_fifth.txt", "w") as f:
    content = f.write(content)
'''






# 6. Write a program to mine a log file and find out whether it contains ‘python’. 
'''
with open("10_files/python_log.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes python is present")
else:
    print("Pyhton is not present")
'''





# 7. Write a program to find out the line number where python is present from ques 6. 
'''
with open("10_files/python_log.txt") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if("python" in line):
        print(f"Python is present in line : {lineNo}")
        break
    lineNo += 1
else:
    print("Pyhton is not present")
'''



# 8. Write a program to make a copy of a text file “this. txt” 
'''
with open("10_files/this.txt") as f:
    content = f.read()

with open("10_files/this_copy.txt", "w") as f:
    f.write(content)
'''





# 9. Write a program to find out whether a file is identical & matches the content of 
# another file. 
'''
f1 = open("10_files/file1.txt")
f2 = open("10_files/file2.txt")

if(f1.read() == f2.read()):
    print("Files are identical")
else:
    print("Files are not identical")
'''





# 10. Write a program to wipe out the content of a file using python. 
'''
with open("10_files/written_file.txt", "w") as f:
    f.write("")
'''



# 11. Write a python program to rename a file to “renamed_by_ python.txt. 

import os

os.rename("10_files/demo.txt", "10_files/renamed_by_python.txt")
