#! python3
# Hangman, just without any image
# Guess the letters of the random word, can only get 5 wrong.

from random_words import RandomWords


def generateWord():
    #return a random word
    return RandomWords().random_word()

def displayWord(word, chances, winner):
    # displays showWords list value to show
    # what letters have been guessed correctly 
    for x in word:
        print(x, end= ' ')
    #display chances left
    print(f"\n{chances} chances left\n")
    #check if user has guessed entire word
    if '_' not in word:
        winner = True
        
def getLetter():
    # get a letter from user and validate input
    while True:
        let = input('Enter a letter (a-z): ')
        if let.isalpha() and len(let) == 1:
            break
        else:
            continue
    return let


def main():
    
    again = '' #loop control
    while again == '':
        winner = False  #flag for if whole word found
        chances = 5     # number of wrong entries left

        # generate random word
        word = generateWord()

        # initiliaze list with '_' in place of letters of the word
        showWord = ['_' for x in word]

        # show how long the word is
        print(f"The word has {len(word)} letters")
        displayWord(showWord, chances, winner)

        # Get letter from user, if letter is not in word chances go down 1
        # If letter in word, showWord list updated from the '_' to the
        # value of the letter found in the correct indexes
        while chances > 0 and winner != True:
            letter = getLetter()
            if letter not in word:
                chances -= 1
            else:
                for x in range(len(word)):
                    if word[x] == letter:
                        showWord[x] = letter

            # display what has been found after every guess
            displayWord(showWord, chances, winner)

        # if all letters found
        if (winner):
            print('You got it!')
            again = input('Press Enter to go again or any other key to quit')
        else:
            print(f"The correct word was {word}")
            again = input('Press Enter to go again or any other key to quit')
            print('\n\n')

#call main
main()
        

