'''
class player():
    
    def __init__(self, number):
        
        self.number = number


class Game
'''

# Rock,Paper, Scissor

# have 3 turns
# tracks player 1 and 2

# rock > scissors 
# scissors > paper
# paper > rock

# takes player 1 input
# takes player 2 input

# compares power of inputs and announces winner

# repeats system until one player reaches a score of 3
# game ends


def introduction():
    
    print("Welcome to the game of Rock,Paper and Scissors.")
    print("Rules:")
    print("You can only choose Rock, Paper or Scissors.")  
    
def winner(playerOneChoice,playerTwoChoice):
    # if player one 
    precedence = ["rock", "paper","scissors"]
    
    # if player1 == pred[smth] and player2 == pred[smth - 1]
    # player 1 wins
    # if player1 ==pred[smth] and player 2 == pred[smth - 2]
    # player 2 wins
    
    playerOnePos = precedence.index(playerOneChoice.lower())
    # if player1 chooses smth and player2 chooses something weaker than him
    if playerOneChoice.lower() == precedence[playerOnePos] and playerTwoChoice.lower() == precedence[playerOnePos]:
        return 0
    
    elif playerOneChoice.lower() == precedence[playerOnePos] and playerTwoChoice.lower() == precedence[playerOnePos - 1]:
        return 1
    
    else:
        return 2    
    
def scores(playerOneWins,playerTwoWins):
    
    print("")
    print("Scores so far:")
    print("Player 1: "+ str(playerOneWins))
    print("Player 2: "+ str(playerTwoWins))
    print("")
        
def winnerAnnouncement(playerOneWins):
    
    if playerOneWins >= 3:
        print("Player One Wins!")
    else:
        print("Player Two Wins!")    

def gameEndingLines():
    
    print("Game Over! Thank you for playing.")    

def main():
    
    introduction()
    
    turns = int(input("Please enter best of how many rounds you'll like to play: "))
    
    playerOneWins = 0
    playerTwoWins = 0
    
    while(playerOneWins < turns and playerTwoWins < turns):
        playerOneChoice = input("Player one chooses: ")
        playerTwoChoice = input("Player two chooses: ")
        
        result = winner(playerOneChoice,playerTwoChoice)
    
        if result == 0:
            pass
        elif result == 1:
            playerOneWins += 1
        else:
            playerTwoWins += 1 
        
        scores(playerOneWins,playerTwoWins)

    winnerAnnouncement(playerOneWins)

    gameEndingLines()

main()