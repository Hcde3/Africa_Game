import random

def applicaple(guess):
    try:
        int(guess)
        print("Incorrect input")
        return True
    except:
        return False
def fileread(b,c):
    f = open(b,"r")
    content = f.readlines()
    return content[c]
    f.close()

blank = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
L0 = """
 -----
 |   |
 0   |
/|\  |
/ \  |
--------"""
L1 = """
 -----
 |   |
 0   |
/|\  |
/    |
--------"""
L2 = """
 -----
 |   |
 0   |
/|\  |
     |
--------"""
L3 = """
 -----
 |   |
 0   |
/|   |
     |
--------"""
L4 = """
 -----
 |   |
 0   |
 |   |
     |
--------"""
L5 = """
 -----
 |   |
 0   |
     |
     |
--------"""
L6 = """
 -----
     |
     |
     |
     |
--------"""
L7 = """

     |
     |
     |
     |
--------"""
L8 = """

     
     
     
     
--------"""

stages = [L0,L1,L2,L3,L4,L5,L6,L7,L8]
on = True
while on:
    chances = 8
    score = 0
    play = True
    wrongguess = []
    dif = input("Difficulty Selection:\nEasy (0)\nMedium (1)\nHard (2)\n")
    choosing = True
    while choosing:
        wnum = random.randint(30,466000)
        word = fileread("words.txt",wnum)
        word = word.strip()
        if dif == "0":
            if len(word) <= 5:
                choosing = False
        if dif == "1":
            if len(word) <= 7 and len(word) >= 4:
                choosing = False
        if dif == "2":
            if len(word) >= 6:
                choosing = False
    cover = ""
    for x in range(len(word)):
        cover = cover + "-"
    while play:
        stage = stages[chances]
        print(blank)
        print(stage)
        print(f"Word: {cover}")
        print(f"Score: {score}")
        print(f"Wrong Guesses: {wrongguess}")
        if chances == 0:
            win = False
            play = False
        elif score == len(word):
            win = True
            play = False
        else:
            NA = True
            while NA:
                letter = input("Guess a letter:  ")
                NA = applicaple(letter)
                    
        
        if letter in word and not letter in cover:
            for x in range(len(word)):
                if word[x] == letter:
                    cover = cover[:x] + letter + cover[x+1:]
                    score += 1
        elif not letter in cover and not letter in word and not letter in wrongguess:
            wrongguess.append(letter)
            chances -= 1
    if win:
        print("Congratulations you won!")
    else:
        print(f"You Lost.\nCorrect word: {word}")
    ans = input("Type (y) to play again\nType (n) to quit\n")
    if ans == "y":
        on = True
    else:
        on = False
            
            
        

