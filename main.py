import random
import words

error = 0
word_guess = random.choice(words.word)
guesses = []
print(word_guess)
while error < 8:
    guess = input("Make a guess: ").lower()
    if len(guess) == 1:
        if guess in guesses:
            print("Already guessed")
        elif guess in word_guess:
            if word_guess.count(guess) > 1:
                for i in range(word_guess.count(guess)):
                    guesses.append(guess)
            else:
                guesses.append(guess)
            print("Yes")
        else:
            print("Wrong")
            error+=1
        if len(guesses) == len(word_guess):
            break
    else:
        print("Letters only")
        continue

print(guesses)