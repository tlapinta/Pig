# Responsible for rendering the messages for the game to the terminal
# Will use the game messages class to create strings to be rendered
import time
import os
import sys
import GameLib.state as state
from GameLib.gameSettings import GameSettings
from GameLib.gameMessages import GameMessages
from Utility.userInput import UserInput

class RenderMessages:

    __cubeFrames = [
        """
███
███
███
        """,
        """
 ██
███
 ██
        """,
        """
  █
 ███
  █
        """,
        """
 ██
███
 ██
        """,
        """
███
███
███
        """
    ]

    # Display the Welcome Message to give the option to learn the rules
    @staticmethod
    def renderWelcomeMessage() -> None:

        #Initialize the Welcome String
        welcomeString = 'Welcome to Pig - The Competetive Dice Game'
        RenderMessages.__printCharByChar(welcomeString)

        # Check to see if the rules should be shown
        if UserInput.getRenderRules():
            RenderMessages.renderRules()
        else:
            RenderMessages.renderGameStart()

    # Displays the rules
    @staticmethod
    def renderRules() -> None:

        # Clear the terminal
        RenderMessages.__clearTerminal()

        # Initialize the rules variable
        rulesString = 'RULES:\n' \
                      '2 Dice are rolled\n' \
                      'Player\'s turns switch back and forth. The sum of their turn is added to their total score\n' \
                      'The objective is to get the total score to be above the final score you set the game to\n' \
                      'A player can choose to continue to roll unless a double is rolled, or either dice roll is a "1"\n' \
                      'If a double is rolled, the total is added to the score and they must roll again\n' \
                      'If a single "1" is rolled, the turn ends and the turn total does not get added to the player\'s overall score\n' \
                      'If a double "1" is rolled, the turn ends and the player\'s score gets set back to "0"'
        
        # Print the rules
        RenderMessages.__printLineByLine(rulesString)

        # Wait to see if the user wants to return or not
        if UserInput.getReturnToMain():
            # Render the Main Menu Screen
            RenderMessages.__clearTerminal()
            RenderMessages.renderWelcomeMessage()

    # Renders the start of the game
    @staticmethod
    def renderGameStart() -> None:

        # Clear the terminal
        RenderMessages.__clearTerminal()

        # Grab and store the game information
        finalScore = UserInput.getFinalScore()
        player2Type = UserInput.getPlayer2Type()
        state.gameSettings = GameSettings(finalScore, player2Type)

        # Clear the terminal
        RenderMessages.__clearTerminal()

        # Print the message
        startGameMessage = 'Let the game commence!'
        RenderMessages.__printCharByChar(startGameMessage)
        time.sleep(.5)

    # Renders the current Game Situation
    @staticmethod
    def renderCurrentGameStatus() -> None:

        # Clear the terminal
        RenderMessages.__clearTerminal()

        # Get the current game stats
        totalScores = GameMessages.getTotalScores()
        turnScores = GameMessages.getTurnScore()
        fullMessage = totalScores + '\n' + turnScores + '\n'

        # Print the message
        print(fullMessage)

    # Renders the current turn score
    def renderTotalScore(newLine: bool) -> None:
        
        # Get the total score message
        turnScore = GameMessages.getTurnScore()

        if newLine:
            print()
        
        # Print the message
        print(turnScore)

    # Renders the Dice Roll
    @staticmethod
    def renderDiceRoll(spins: int = 5, delay: float = 0.1) -> None:
        
        frames = RenderMessages.__cubeFrames
        frame_height = len(frames[0].splitlines())

        # Print the first frame normally
        print(frames[0])
        time.sleep(delay)

        for _ in range(spins):
            for frame in frames[1:]:
                # Move cursor up to overwrite previous frame
                sys.stdout.write(f"\033[{frame_height}A")
                sys.stdout.flush()
                # Print the new frame
                print(frame)
                time.sleep(delay)
        
        # Clear the cube after animation
        sys.stdout.write(f"\033[{frame_height}A") 
        sys.stdout.flush()

        for _ in range(frame_height):
            print(" " * 40) 
            
        sys.stdout.write(f"\033[{frame_height}A")
        sys.stdout.flush()

    # Renders the resulting dice roll to the user
    @staticmethod
    def renderDiceResult(dice1: int, dice2: int) -> None:

        # Grab the test for the dice roll
        text = GameMessages.getDiceRoll(dice1, dice2)

        # Print the result char by char
        RenderMessages.__printCharByChar(text)

    # Renders the message telling the user their turn ended and score is to be cleared
    @staticmethod
    def renderClearScoreMessage() -> None:

        # Get the clear score message
        text = GameMessages.getClearScoreMessage()

        # Print the result char by char
        RenderMessages.__printCharByChar(text)

    # Renders the end turn message telling the user their turn is over
    @staticmethod
    def renderEndTurnMessage() -> None:

        # Get the end turn message
        text = GameMessages.getEndTurnMessage()

        # Print the result char by char
        RenderMessages.__printCharByChar(text)
    
    # Gets the cubes for animation
    @classmethod
    def getCubes(cls) -> list[str]:
        return cls.__cubeFrames
    
    # Display effect for char by char text appearance
    @staticmethod
    def __printCharByChar(text: str, delay: float = .025) -> None:

        # Split the words into a list of chars
        chars = list(text)

        # Iterate using a for-each loop
        for char in chars:
            print(char, end = "", flush = True)
            time.sleep(delay)
        print()

    # Display effect for line by line text apperance
    @staticmethod
    def __printLineByLine(text: str, delay: float = .1) -> None:

        # Split the string into a list of strings by \n
        lines = text.split('\n')

        # Iterate using a for-each loop
        for line in lines:
            print(line, flush = True)
            time.sleep(delay)
        print()

    # Clears the terminal
    @staticmethod
    def __clearTerminal():

        # Check if the terminal is Windows
        if os.name == 'nt':
            # Windows
            os.system('cls')
        else :
            # Linux
            os.system('clear')
