import random


def hangman():
    words = random.choice(
        ["hulk", "thor", "hawkeye", "falcon", "vision", "thanos", "loki", "groot", "gamora", "wong", "nebula"])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    while len(words) > 0:
        main = ""
        missed = 0
        for letter in words:
            if letter in guessmade:
                main += letter
            else:
                main += "_" + ""
        if main == words:
            print(main)
            print("You win!")
            break
        print("Guess the word :", main)
        guess = input()
        if guess in validletters:
            guessmade += guess
        else:
            print("Enter a valid character")
            guess = input()
        if guess not in words:
            turns -= 1
            if turns == 9:
                print(f"{turns} turns left")
                print("~~~~~~~~~~~")
            if turns == 8:
                print(f"{turns} turns left")
                print("~~~~~~~~~~~")
                print("     o     ")
            if turns == 7:
                print(f"{turns} turns left")
                print("~~~~~~~~~~~")
                print("     o     ")
                print("     |     ")
            if turns == 6:
                print(f"{turns} turns left")
                print("~~~~~~~~~~~")
                print("     o     ")
                print("     |     ")
                print("    /      ")
            if turns == 5:
                print(f"{turns} turns left")
                print("~~~~~~~~~~~")
                print("     o     ")
                print("     |     ")
                print("    / \    ")
            if turns == 4:
                print(f"{turns} turns left")
                print("~~~~~~~~~~~")
                print("   \ o     ")
                print("     |     ")
                print("    / \    ")
            if turns == 3:
                print(f"{turns} turns left")
                print("~~~~~~~~~~~")
                print("   \ o /   ")
                print("     |     ")
                print("    / \    ")
            if turns == 2:
                print(f"{turns} turns left")
                print("~~~~~~~~~~~")
                print("   \ o /|  ")
                print("     |     ")
                print("    / \    ")
            if turns == 1:
                print(f"{turns} turns left")
                print("Last breathes counting. Take care!")
                print("~~~~~~~~~~~")
                print("   \ o_|/   ")
                print("     |     ")
                print("    / \    ")
            if turns == 0:
                print("You lose")
                print("You let a kind man die.")
                print("~~~~~~~~~~~")
                print("     o_|   ")
                print("    /|\    ")
                print("    / \    ")
                print("The word was", words)
                break


name = input("Enter you name : ")
print("Hello,", name)
print("~~~~~~~~~~~~~~~~~~~~")
print("Try to guess the word in less than 10 attempts")
hangman()
print()
