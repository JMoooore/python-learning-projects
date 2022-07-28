def game():
    # Ask if user wants to play
    playAgain = newgame()

    while playAgain:
        # Ask user if they want to be X's or O's
        markers = chooseAMarker()
        gameboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        gameOver = False
        player = 2
        while not gameOver:
            # Switch the players turn
            if player == 1:
                player = 2
            else: 
                player = 1
            # Ask player where they want to place a value
            gameboard = placeMarker(player, markers, gameboard)
            # Display the gameboard
            displayGameboard(gameboard)
            # Check if that was the winning move
            gameOver = checkGameOver(gameboard)
        print(f'Game Over! Player {player} won!' )
        # Ask user if they want to play again
        playAgain = newgame()

def newgame():
    answer = 'filler'
    while (answer.lower()[0] != 'n'):
        answer = input('Do you want to play Tic-Tac-Toe (Y or N)?')
        if (answer.lower()[0] == 'y'):
            return True

def chooseAMarker():
    answer = 'filler'
    while (answer.lower()[0] != 'x' or answer.lower()[0] != 'o'):
        answer = input('Player 1 do you want to be X or O?')
        if (answer.lower()[0] == 'x'):
            return ('X','O')
        elif (answer.lower()[0] == 'o'):
            return ('O','X')

def placeMarker(player, markers, gameboard):
    answer = ''
    checkList = []
    for x in range(len(gameboard)):
        # create a list of possible guesses
        if gameboard[x] == ' ':
            checkList.append(str(x+1))
    while answer not in checkList:
        answer = input(f'Player {player}, choose an unoccupied location to place a marker [1-9]?')
    
    gameboard[int(answer) - 1] = markers[player - 1]
    return gameboard

def displayGameboard(gameboard):
    print(f'''
        {gameboard[0]} | {gameboard[1]} | {gameboard[2]}
        --------------------
        {gameboard[3]} | {gameboard[4]} | {gameboard[5]}
        --------------------
        {gameboard[6]} | {gameboard[7]} | {gameboard[8]}
        '''
    )

def checkGameOver(gameboard):
    # Check Diagonals
    if gameboard[0] == 'X' or gameboard[0] == 'O':
        if gameboard[0] == gameboard[4] and gameboard[0] == gameboard[8]:
            return True
    elif gameboard[1] == 'X' or gameboard[1] == 'O':
        if gameboard[1] == gameboard[4] and gameboard[1] == gameboard[7]:
            return True
    elif gameboard[2] == 'X' or gameboard[2] == 'O': 
        if gameboard[2] == gameboard[4] and gameboard[2] == gameboard[5]:
            return True
    # Check Verticals
    for x in range(0,3):
        if gameboard[x] == 'X' or gameboard[x] == 'O':
            if gameboard[x] == gameboard[x+3] and gameboard[x] == gameboard[x+6]:
                return True
    # Check Horizontals
    for x in range(0,7,3):
        if gameboard[x] == 'X' or gameboard[x] == 'O':
            if gameboard[x] == gameboard[x+1] and gameboard[x] == gameboard[x+2]:
                return True
    return False
        

game()