import random

eassy_words = ["apple","train","tiger","money","pakistan"]
medium_words = ["python","monkey","planet","laptop"]
hard_words = ["elephant","diamond","gold","computer","monitor"]

print("Welcome to Password Gussing Game:")
print("Chooose Difficulty level :Easy , Medium or Hard")

level=input('Enter Difficulty:').lower()
if level=="easy":
    secret=random.choice(eassy_words)
elif level=="medium":
    secret=random.choice(medium_words)
elif level=="hard":
    secret=random.choice(hard_words)
else:
    print("invalid chiuce.defaulting to easy level")
    secret=random.choice(eassy_words)

attempts=0
print("\n Guess the secret password: ")

while True:
    guess =input("Enter your Guess: ").lower()
    attempts +=1

    if guess == secret:
        print(f'Congrats! You Guessed it in {attempts} attempts')
        print ("game is over!")
        break

    hint =""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint +="_"
    
    print("hint" , hint)
   