# Retrieves the inputs the user provided in order to play the game
# Assumes game is always a 2 player game with a real user of computer

class UserInput:
    __validTypes = ['computer', 'human']

    # Retrieves the list of valid player types
    @classmethod
    def getValidTypes(cls) -> list[str]:
        return cls.__validTypes
    
    # Retrieves if the user wants rules or to continue
    @staticmethod
    def getRenderRules() -> bool:
        
        # Prompt until valid selection
        while True:
            seeRules = input('Would you like to see the rules? (Y/N): ').lower()

            if seeRules == 'y':
                return True
            elif seeRules == 'n':
                return False
            else:
                print('You must answer with the following: (Y/N)\n')
                
    # Retrieves the type of Player 2 (Human/Computer)
    @staticmethod
    def getPlayer2Type() -> str:
        validTypes = UserInput.getValidTypes()

        # Prompts until valid player is chosen
        while True:   
            playerType = input('Select the following player type for player 2 ("Computer" or "Human"): ').lower()

            # Check if the type is a valid type
            if playerType not in validTypes:
                print('Invalid type please try again\n')
            else:
                return playerType

    # Retrieves the score the game should be played to
    @staticmethod
    def getFinalScore() -> int:

        # Prompts until valid player is chosen
        while True:

            # Check if the value is an Integer
            try:
                scoreLimit = int(input('Select a score to play to, (must be at least 50): '))
                
                # Check if the score is at least 50
                if scoreLimit >= 50:
                    return scoreLimit
                else:
                    print('Score must be greater than 50, please try again\n')
            except ValueError:
                print('Value selected is not a numerical value, please try again\n')
