# Renders the messages for specific situations
# EX: Score Updates, Player turn results

import GameLib.state as state

class GameMessages:

    # Returns the string representation of the total scores
    @classmethod
    def getTotalScores(cls) -> str:
        # Grabs the stored values in the game settings
        player1Score = state.gameSettings.getPlayer1TotalScore()
        player2Score = state.gameSettings.getPlayer2TotalScore()

        # Return the string representation of the score
        return f'Player 1 Score: {player1Score} ----- Player 2 Score: {player2Score}'
    
    # Returns the string representation of the turn score for the current turn
    @classmethod
    def getTurnScore(cls) -> str:
        # Grabs the stored values in the game settings
        currentTurn = state.gameSettings.getCurrentTurn()
        turnScore = state.gameSettings.getPlayer1TurnScore() if currentTurn == 'Player 1' else state.gameSettings.getPlayer1TurnScore()

        # Returns the string representation of the turn score
        return f'Turn Score For {currentTurn}: {turnScore}'

