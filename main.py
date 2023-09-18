import requests

def generate():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    word_guess = response.json()[0]
    return word_guess

def draw(error):
    if error == 0:
        print("----------\n|\n|\n|\n|\n|\n|")
    elif error == 1:
        print("----------\n|        |\n|\n|\n|\n|\n|")
    elif error == 2:
        print("----------\n|        |\n|        O\n|\n|\n|\n|")
    elif error == 3:
        print("----------\n|        |\n|        O\n|        |\n|\n|\n|")
    elif error == 4:
        print("----------\n|        |\n|        O\n|       /|\n|\n|\n|")
    elif error == 5:
        print("----------\n|        |\n|        O\n|       /|\\\n|\n|\n|")
    elif error == 6:
        print("----------\n|        |\n|        O\n|       /|\\\n|       /\n|\n|")
    elif error == 7:
        print("----------\n|        |\n|        O\n|       /|\\\n|       / \\\n|\n|")

def main():
    error = 0
    count = 0
    guesses = []
    indices = []

    while error < 8:
        if count == 0: # start
            word_guess = generate()
            list = ['_' for _ in word_guess]
            print(' '.join(list))

        draw(error)
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
                print(' '.join(list))
                error+=1

            if len(guesses) == len(word_guess): # if player wins
                print(f"You guessed the word: {word_guess}")
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
        if error == 6:
            print("Last try!")

        count+=1  
    if error == 7:
        draw(error)
        print(f"You ran out of tries, the word is {word_guess.upper()}")

if __name__ == '__main__':
    main()