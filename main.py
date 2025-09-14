# main.py
from Utility.userInput import UserInput
from GameLib.gameSettings import GameSettings
import GameLib.state as state   # import the module
from GameLib.gameMessages import GameMessages

def main():
    # Initialize variables to store for game settings
    player2Type = UserInput.getPlayer2Type()
    finalScore = UserInput.getFinalScore()

    # Update the gameSettings variable in the state module
    state.gameSettings = GameSettings(finalScore, player2Type)

    print(GameMessages.getTotalScores())

if __name__ == "__main__":
    main()
