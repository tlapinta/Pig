# Acts as the game engine to drive the outputs and flows
from Utility.userInput import UserInput
from Utility.renderMessages import RenderMessages
import GameLib.state as state
import random

class GameEngine:

    # Method to begin the game
    @staticmethod
    def executeGame() -> None:

        # Loop to continue game until max score reached (TODO)
        while True:

            # Determine if the user wants to role
            if UserInput.getRole():

                # Execute Roll
                dice1, dice2 = GameEngine.__rollDice()

                # Determine which the outcome should be
                if (GameEngine.__canRollAgain(dice1, dice2)):

                    # Add to the turn
                    GameEngine.__addToTurnScore(dice1, dice2)

                    # Render the message to update the turn score
                    RenderMessages.renderTotalScore()
                elif (GameEngine.__scoreToBeCleared(dice1, dice2)):
                    GameEngine.__clearScoreAndSwitch()
                else:
                    GameEngine.__endTurnAndSwitch()
            else: 
                
                # Set the turn to the next turn
                GameEngine.__switchTurn()

    # Simulate the roll of the dice
    @staticmethod
    def __rollDice() -> tuple[int, int]:

        # Render the dice roll visual
        RenderMessages.renderDiceRoll()
        
        # Grab random dice values
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        # Print the dice roll result
        RenderMessages.renderDiceResult(dice1, dice2)

        # Return the values
        return dice1, dice2
    
    # Determine if the user can roll again based on dice result
    @staticmethod
    def __canRollAgain(dice1: int, dice2: int) -> bool:
        return (dice1 == 1) or (dice1 == 1)
    
    # Determine if the score needs to be cleared
    @staticmethod
    def __scoreToBeCleared(dice1: int, dice2: int) -> bool:
        return (dice1 == 1) and (dice2 == 1)
    
    # Clear the score and change the turn
    def __clearScoreAndSwitch() -> None:

        # Render the message
        RenderMessages.renderClearScoreMessage()

        # Get the current player to determine which score to clear
        currentTurn = state.gameSettings.getCurrentTurn()

        match currentTurn:
            case 'Player 1':
                state.gameSettings.setPlayer1TotalScore(0)
            case 'Player 2':
                state.gameSettings.setPlayer2TotalScore(0)

        GameEngine.__switchTurn()

    # Clear the turn and switch
    def __endTurnAndSwitch() -> None:

        # Render the message
        RenderMessages.renderEndTurnMessage()

        # Switch the turn
        GameEngine.__switchTurn()
    
    # Method to clear the turn score and switch the turn
    def __switchTurn() -> None:

        # Get the current player to determine which score to clear
        currentTurn = state.gameSettings.getCurrentTurn()

        match currentTurn:
            case 'Player 1':
                state.gameSettings.setPlayer1TurnScore(0)
                state.gameSettings.setCurrentTurn('Player 2')
            case 'Player 2':
                state.gameSettings.setPlayer2TurnScore(0)
                state.gameSettings.setCurrentTurn('Player 1')

    # Adds the resulting roll to the turn score
    def __addToTurnScore(dice1: int, dice2: int) -> None:

        # Add the dice rolls together
        totalRoll = dice1 + dice2

        # Update the turn score
        currentTurn = state.gameSettings.getCurrentTurn()

        match currentTurn:
            case 'Player 1':
                currentScore = state.gameSettings.getPlayer1TurnScore()
                newTurnScore = currentScore + totalRoll
                state.gameSettings.setPlayer1TurnScore(newTurnScore)
            case 'Player 2':
                currentScore = state.gameSettings.getPlayer2TurnScore()
                newTurnScore = currentScore + totalRoll
                state.gameSettings.setPlayer2TurnScore(newTurnScore)
