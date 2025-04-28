import random

def giveHint(word):
    print("Hint: ",end="")
    if word in categorizes[0]:
        print("Famous Person")
    if word in categorizes[1]:
        print("Location")
    if word in categorizes[2]:
        print("Music Name")

categorizes = (("Stephen Curry","Ana de Armas")
               ,("San Fransisco","Londra")
               ,("You are Not Alone", "BAND4BAND"))
chance = 5
word = random.choice(categorizes[random.randint(0,2)])
placeholder = ""
for letter in word:
    if letter == " ":
        placeholder = placeholder + " "
    else:
        placeholder = placeholder + "_"
giveHint(word)

while (chance > 0):
    print(placeholder)
    letter = input("Letter: ").lower()
    if letter in word.lower():
        for index in range(len(word)):
            if word[index].lower() == letter:
                 placeholder = placeholder[:index] + word[index] + placeholder[index+1:]

    else:
        chance -= 1
        print(f"Incorrect guess. {chance} chances left.")
    if "_" not in placeholder:
        print("You Won!")
        break
if "_" in placeholder:
    print(f"You Lost. The word was {word}")
        
       
