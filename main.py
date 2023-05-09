class Main:
    # Hidden member of MyClass
    __word = ""                                                                                                 # Stores the word which needs guessing
    __winState = 0                                                                                              # Stores the win state
    __wordState = ""                                                                                            # Stores what we have guessed correctly
    __guessCount = 0                                                                                            # Stores how many guesses we have done
    __currentGuess = "u"                                                                                        # Stores our last guess

    # Getter for private variable winState
    def getwinstate(self):
        return self.__winState                                                                                  # A getter so we can check the win state outside the class

    # Check if we won based on variable winState
    def checkwin(self):
        if self.__wordState == self.__word:                                                                     # Set the winstate to true (1) if the words are the same
            self.__winState = 1
        else:                                                                                                   # Else make sure the winstate stays on false (0)
            self.__winState = 0

    # A member method that subtracts counts __guessCount
    def modguesscount(self, value, operator):
        if operator == "-":                                                                                     # If "-" then we want to subtract a guess
            self.__guessCount -= value
        elif operator == "+":                                                                                   # If "+" then we want to add a guess
            self.__guessCount += value
        elif operator == "=":                                                                                   # If "=" then we want to set X guesses
            self.__guessCount = value

    # Prints the amount of guesses left
    def printguesscount(self):
        print('You have ' + str(self.__guessCount) + ' guesses left')                                           # Print guesses left
        if self.__guessCount <= 0 and self.__winState == 0:                                                     # Check if we have any guesses left, if not we lose
            print('You lost the game, the word was ' + self.__word)
            exit()

    # Makes us able to guess a letter
    def guess(self, letter):
        try:
            self.__currentGuess = letter.lower()                                                                # Set our current guess
            index = self.__word.index(self.__currentGuess)                                                      # Check the length of our guess
            self.modguesscount(1, "-")                                                                          # Remove one guess as we just guessed
        except ValueError:
            print("Wrong Guess")                                                                                # Print if our guess is not present in the word we need to guess
            self.printguesscount()                                                                              # Print our guesses left
        else:
            self.__wordState = self.__wordState[:index] + self.__currentGuess + self.__wordState[index + 1:]
            print(self.__wordState)                                                                             # Print what we have guessed
            self.printguesscount()                                                                              # Print our guesses left
            self.checkwin()                                                                                     # Check if we won with our last guess

    # Sets up the game of hangman
    def setup(self):
        print("Set a word to be guessed")
        self.__word = input().lower()                                                                           # Make the word which needs to be guessed lowercase
        self.__wordState = "_" * len(self.__word)                                                               # Make the word blank again, in case it is not
        self.modguesscount(0, "=")                                                                              # (Re)set guesses to 0, in case it is not
        self.modguesscount(len(self.__word) + 3, "+")                                                           # You have always 3 extra guesses then the word length

        print('Setup complete, the word is ' + str(len(self.__word)) + ' long')                                 # Print that the setup is done
        print('You have ' + str(self.__guessCount) + ' guesses')                                                # Print how many guesses we have
        print(self.__wordState)                                                                                 # Print the blank spaces
        print()                                                                                                 # Print a blank line so the setup is loose from the guess prints


# Driver code
# Create our main
if __name__ == '__main__':
    main = Main()                                                                                               # Make a new instance so we can call the nessesary functions
    main.setup()                                                                                                # Setup hangman
    while main.getwinstate() != 1:                                                                              # As long as we didn't win we want to guess
        print("Guess a letter - If its a word only the first caracter counts")                                  # Print that we are able to guess
        main.guess(input()[0])                                                                                  # Let the user input a guess but limit it to one character
    print('You guessed the word! You won!')                                                                     # If the while loop is exited it means they won
