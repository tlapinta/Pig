# Import Statements
from Utility.userInput import UserInput
from GameLib.gameSettings import GameSettings
from GameLib.state import gameSettings

def main():
    # Initialize variables to store for game settings
    player2Type = UserInput.getPlayer2Type()
    finalScore = UserInput.getFinalScore()

    gameSettings = GameSettings(finalScore, player2Type)

if __name__ == "__main__":
    main()