# Acts as the game engine to drive the outputs and flows
from Utility.userInput import UserInput
from Utility.renderMessages import RenderMessages
import GameLib.state as state
import random

class GameEngine:

    # Method to begine the game
    @staticmethod
    def executeGame() -> None:

        # Determine if the user wants to role
        if UserInput.getRole():

            # Execute Roll
            dice1, dice2 = GameEngine.__rollDice()
        else: 
            
            # Set the turn to the next turn
            state.gameSettings.setCurrentTurn('Player 2')

    def __rollDice() -> tuple[int, int]:
        RenderMessages.renderDiceRoll()
        
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        RenderMessages.renderDiceResult(dice1, dice2)

        return dice1, dice2