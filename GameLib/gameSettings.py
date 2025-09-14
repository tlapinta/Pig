# Stores the game settings and scores for reference

class GameSettings:
    # Total Scores
    __player1TotalScore = None
    __player2TotalScore = None

    # Turn Scores
    __player1TurnScore = None
    __player2TurnScore = None

    # Settings
    __finalScore = None
    __player2Type = None
    __currentTurn = None

    # Class Init Method 
    def __init__(self, finalScore, player2Type):
        self.__player2Type =  player2Type
        self.__finalScore = finalScore
        self.__player1TotalScore = 0
        self.__player2TotalScore = 0
        self.__player1TurnScore = 0
        self.__player2TurnScore = 0
        self.__currentTurn = 'Player 1'

    # Getter Methods
    def getPlayer1TotalScore(self) -> int:
        return self.__player1TotalScore
    
    def getPlayer2TotalScore(self) -> int:
        return self.__player2TotalScore
    
    def getPlayer1TurnScore(self) -> int:
        return self.__player1TurnScore
    
    def getPlayer2TurnScore(self) -> int:
        return self.__player2TurnScore
    
    def getFinalScore(self) -> int:
        return self.__finalScore
    
    def getPlayer2Type(self) -> str:
        return self.__player2Type
    
    def getCurrentTurn(self) -> str:
        return self.__currentTurn
    
    # For debugging
    def getAllSettings(self) -> dict:
        return {k: v for k, v in self.__dict__.items()}
    
