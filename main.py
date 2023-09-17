import random
import words

def generate():
    word_guess = random.choice(words.word)
    return word_guess

def main():
    error = 0
    count = 0
    guesses = []
    indices = []

    while error < 8:
        if count == 0:
            word_guess = generate()
            print(word_guess)
            list = ['_' for _ in word_guess]
            print(' '.join(list))

        guess = input("Make a guess: ").lower()

        if len(guess) == 1: # checks if the guess is a single char
            if guess in guesses:
                print("Already guessed")
            elif guess in word_guess:
                if word_guess.count(guess) > 1:
                    for i in range(word_guess.count(guess)):
                        guesses.append(guess)
                    for i in range(len(word_guess)):
                        if word_guess[i] == guess:
                            indices.append(i)
                    for i in indices:
                        list[i] = guess
                    indices.clear()
                    print(' '.join(list))
                else:
                    guesses.append(guess)
                    print("Yes")
                    list[word_guess.index(guess)] = guess
                    print(' '.join(list))
            else:
                print("Wrong")
                error+=1

            if len(guesses) == len(word_guess): # if player wins
                print(guesses)
                try_again = input("Try again? y/n: ").lower()
                if try_again == 'y':
                    error = 0
                    guesses.clear()
                    count = 0
                    continue
                else:
                    break
        else:
            print("Letters only") 
        count+=1

if __name__ == '__main__':
    main()