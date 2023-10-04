def rps(p1, p2):
    def player1(p1):
        if p1 == 'rock':
            player1 = 2
            return player1
        elif p1 == 'scissors':
            player1 = 1
            return player1
        elif p1 == 'paper':
            player1 = 0
            return player1
        
    def player2(p2):
        if p2 == 'rock':
            player2 = 2
            return player2
        elif p2 == 'scissors':
            player2 = 1
            return player2
        elif p2 == 'paper':
            player2 = 0
            return player2
        
    
    if player1(p1) == 0 and player2(p2) == 2:
        return 'Player 1 won!'
    elif player2(p2) == 0 and player1(p1) == 2:
        return 'Player 2 won!'


    if player1(p1) > player2(p2):
        return "Player 1 won!"
    elif player2(p2) > player1(p1):
        return "Player 2 won!"
    elif player1(p1) == player2(p2):
        return "Draw!"

print(rps('rock', 'paper'))