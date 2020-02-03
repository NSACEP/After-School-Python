import random

def choose_word():
    f = open("words.txt","r+")
    l = []
    for line in f:
        l.append(line.replace("\n",""))
    f.close()
    word = random.choice(l)
    return word

def display(word,turns):
    print(f"Turns remaining: {turns}/6")
    print("Word: "+"*"*len(word))

turns = 6
word = choose_word()
wordList = ["*" for i in word]

while turns > 0:
    display(word, turns)
    guess_number = int(input("Which letter (please enter an integer): "))
    guess_letter = input("Guess the letter (please enter a letter): ")
    if word[guess_number] == guess_letter:
        pass
    else:
        turns = turns - 1

