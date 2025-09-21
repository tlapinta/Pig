# main.py
from Utility.renderMessages import RenderMessages
from GameLib.gameEngine import GameEngine

def main():
    # Main Menu Message
    RenderMessages.renderWelcomeMessage()

    # Set the starting game settings
    GameEngine.executeGame()
    
if __name__ == "__main__":
    main()
