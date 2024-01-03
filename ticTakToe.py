board = ["_","_","_",
         "_","_","_",
         "_","_","_"]
player = 'X'
game_on = True
winner = None

# Print game board
def printBoard(board):
    print("\n")
    print("BOARD:")
    print("\n")

    for i in range(0,9,3):
        print( board[i] + " | "+ board[i+1] + " | "+ board[i+2] )
    print("\n")


# take player input
def takeInput(player, board):
    validInput=True
    while( validInput ):

        print("PLAYER: " + player)
        index = int(input("Enter position "))

        if( board[index] != '_' ):
            print("\nINVALID INPUT")
            print("Enter again\n")

            validInput = True
        else:
            validInput = False

    if( player == 'X' ):
        board[index]='0'
    else:
        board[index]='X'

# check game status: win, Tie or continue 
def checkStatus(board, winner, game_on):
    f=0
    # horizontal check
    for i in range(0,9,3):
        if( (board[i] == board[i+1] == board[i+2]) and board[i] != '_' ):
            if( board[i] == '0' ):
                winner = 'X'
            else:
                winner = 'Y'
            game_on = False
            return {winner, game_on}    
    # vertical check
    for i in range(0,3):
        print(i, i+3, i+6)
        if( (board[i] == board[i+3] == board[i+6]) and board[i] != '_' ):
            if( board[i] == '0' ):
                winner = 'X'
            else:
                winner = 'Y'
            game_on = False
            return {winner, game_on}
    
    # diagonal check
    k=4
    for i in range(0,3,2):
       if( (board[i] == board[i+k] == board[i+2*k]) and board[k] != '_' ):
            if( board[i] == '0'):
                winner ='X'
                game_on = False
            else:
                winner ='Y'
                game_on = False
            return {winner, game_on} 
       k=k//2

    if '_' not in board:
        winner = 'T'
        game_on = False


    return {winner, game_on}
    
# switch player
def switchPlayer(player):   
    if( player == 'X' ):
        player='Y'
    else:
        player='X'
    return player

while( game_on == True ):
    printBoard(board)
    takeInput(player, board)
    status = checkStatus(board, winner, game_on)
   
    status = list(status)
    game_on=status[0]
    winner=status[1]
   
    player = switchPlayer(player)
printBoard(board)

if( status[1] == 'T' ):
    print("GAME RESULT: TIE")
else:
    print(f"GAME RESULT: {status[1]} WINS")





class TicTakToe:
    def __init__(self):
        self.board = ["_","_","_",
         "_","_","_",
         "_","_","_"]
        
    def displayBoard(self):
        print("\n")
        for i in range(0,9,3):
            print( self.board[i] + " | "+ self.board[i+1] + " | " + self.board[i+2] )
        print("\n")

    def updateBoard(self, index, symbol):
        # print(type(index))
        if( index >=0 and index <= 8 and self.board[index]=='_'):
            self.board[index]= symbol
        else: 
            print("INVALID INPUT")


    def checkWin(self):
        winner=None

         # horizontal check
        game_on = True
        for i in range(0,9,3):
            if( (self.board[i] == self.board[i+1] == self.board[i+2]) and self.board[i] != '_' ):
                if( self.board[i] == '0' ):
                    winner = '1'
                else:
                    winner = '2'
                game_on = False
                return {winner, game_on}  
            
        # vertical check
        for i in range(0,3):
            if( (self.board[i] == self.board[i+3] == self.board[i+6]) and self.board[i] != '_' ):
                if( self.board[i] == '0' ):
                    winner = '1'
                else:
                    winner = '2'
                game_on = False
                return {winner, game_on}
        
        # diagonal check
        k=4
        for i in range(0,3,2):
            if( (self.board[i] == self.board[i+k] == self.board[i+2*k]) and self.board[k] != '_' ):
                    if( self.board[i] == '0'):
                        winner ='1'
                        game_on = False
                    else:
                        winner ='2'
                        game_on = False
                    return {winner, game_on} 
            k=k//2
        if '_' not in self.board:
            winner = 'T'
            game_on = False


        return {winner, game_on}

class player:

    def __init__(self, name, symbol):
        self.name=name 
        self.symbol = symbol
    def takeINput(self):
        print(f"PLAYER: {self.name}")
        index = int( input("Enter index: ") )
        return index


game_on=True

n1 = input("\nFirst Player:  Enter your name: ")
player1 = player(n1,'0')

n2 =  input("Second Player:  Enter your name: ")
player2 = player(n2,'X')

game = TicTakToe()
while( game_on ):
    game.displayBoard()

    index = player1.takeINput()
    game.updateBoard(index,'0')

    game.displayBoard()

    result = game.checkWin()
    result = list(result)
    game_on= result[0]

    if( game_on ):
        index = player2.takeINput()
        game.updateBoard(index, 'X')
        game.displayBoard()

    result = game.checkWin()
    result = list(result)
    game_on= result[0]
    

result = game.checkWin()
result = list(result)
if( result[1] == 'T' ):
    print("TIE")
elif( result[1] == '1' ):
    print(f"WINNER IS: {player1.name}")
else:
    print(f"WINNER IS: {player2.name}")

    


