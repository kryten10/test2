import random

def main():
    words = ["write", "that", "program"]
    chosen_word = []
    hidden_word = []
    guessed_word = []
    chosen_word = random.choice(words)
    blank = len[chosen_word] * ["*"]
    correctguesses = 0
    while correctguesses < len(chosen_word):
        letter = input("enter a letter for the word: ")
        if letter in guessed_word:
            print("got one")
        elif letter not in guessed_word:
            print("try again")






