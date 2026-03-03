# 11_hangman.py
import random

words = ["python", "developer", "shadowfox"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    letter = input("Guess letter: ")

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        print("Wrong guess. Attempts left:", attempts)

if "_" not in guessed:
    print("You won!")
else:
    print("You lost. Word was:", word)
