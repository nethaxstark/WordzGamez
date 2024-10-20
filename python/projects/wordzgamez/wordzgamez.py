import random

game_name = "WordzGamez"
misplaced_letters = []
incorrect_letters = []
max_turns = 5
turns_taken = 0

word_bank = []

with open("a:\Coding\python\projects\wordzgamez\words.txt", "r") as word:
    for x in word:
        word_bank.insert(0,x.strip())
        
        
random_word = random.choice(word_bank).lower()

#print(random_word.strip())

#Game initial starting!

print("Welcome to the "+ game_name)
print("There are total {} letters in the word guess!".format(len(random_word)))


#Input from user.

while max_turns > turns_taken:
    user_guess = input("Guess a word: ")
    if not user_guess.isalpha() or len(user_guess) != len(random_word):
        print("Enter a valid word of length: {}".format(len(random_word)))
        continue
    turns_taken += 1
    
#characters information

    index = 0
    for s in user_guess:
        if s == random_word[index]:
            print(s, end=" ")
        elif s in random_word:
            if s not in misplaced_letters:
                misplaced_letters.append(s)
            print("_", end=" ")
        else:
            if s not in incorrect_letters:
                incorrect_letters.append(s)
            print("_", end=" ")
        
        index += 1

    print("\n")
    print("Misplaced Letters:", misplaced_letters)
    print("Incorrect Letters:", incorrect_letters)
    
    if user_guess.lower() == random_word:
        print("Congratulations You Won!")
        break
    else:
        print("You have {} turns left!".format(max_turns - turns_taken))
        
if max_turns<=turns_taken:
        print("Sorry you are out of turns! The word was {}".format(random_word))
    
