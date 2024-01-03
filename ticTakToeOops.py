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

    


