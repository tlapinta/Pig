# Retrieves the inputs the user provided in order to play the game
# Assumes game is always a 2 player game with a real user of computer

class UserInput:
    __validTypes = ['computer', 'human']

    # Retrieves the list of valid player types
    @classmethod
    def getValidTypes(cls) -> list[str]:
        return cls.__validTypes

    # Retrieves the type of Player 2 (Human/Computer)
    def getPlayer2Type() -> str:
        validTypes = UserInput.getValidTypes()

        # Prompts until valid player is chosen
        while True:   
            playerType = input('SELECT THE FOLLOWING PLAYER TYPE FOR PLAYER 2 ("Computer" or "Human")').lower()

            # Check if the type is a valid type
            if playerType not in validTypes:
                print('INVALID PLAYER TYPE, PLEASE TRY AGAIN\n')
            else:
                return playerType

    # Retrieves the score the game should be played to
    def getFinalScore() -> int:

        # Prompts until valid player is chosen
        while True:

            # Check if the value is an Integer
            try:
                scoreLimit = int(input('SELECT A SCORE TO PLAY TO, (MUST BE AT LEAST 50)'))
                
                # Check if the score is at least 50
                if scoreLimit >= 50:
                    return scoreLimit
                else:
                    print('SCORE MUST BE GREATER THAN 50, PLEASE TRY AGAIN\n')
            except ValueError:
                print('VALUE SELECTED IS NOT A NUMERICAL VALUE, PLEASE TRY AGAIN\n')
