from Board import Players
import array as arr

class Tictactoe:
    brd = ['-',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    turn = 'O'
    counter = 1
    choice=25
     
    def gameplay(self):
        for i in range(1,9):
            choice_arr =[25,25,25,25,25,25,25,25,25,25,25]          #garbage value of array to store choices
            choice = int(input("Player '"+ self.turn +"' Choose a coordinate:"))
            choice_arr[i]= self.choice
            for j in range(0,10):
                if choice != choice_arr[j]:
                    self.brd[choice] =self.turn
                    ppp=Players()
                    ppp.printinfo(self.brd)
                    # self.print_board(self.brd)
                    self.DefConditions(self.brd,self.counter)
                    self.counter += 1
                    self.choice = 25
                    break
                else:
                    print("Wrong coordinate chosen!!!")
            # we have to change the player after every move.
            if self.turn =='X':
                self.turn = 'O'
            else:
                self.turn = 'X'


    def rulebook(self):
            print("Tic-tac-toe is a two player game.\nPlayer one is '0' and Player 2 is 'X'")
            print(" The objective is to satisfy one of the defined Winning condition...")
            print("Coordinates are as follows:\n")
            print('1' + "  |  "+ '2' + "  |  "+ '3')
            print("-"*14)
            print('4' + "  |  "+ '5' + "  |  "+ '6')
            print("-"*14)
            print('7' + "  |  "+ '8' + "  |  "+ '9')
            tt=Tictactoe()
            tt.gameplay()


    def DefConditions(self,brd,counter):  
        if self.counter == 9:
            self.declareDraw(self)

        elif self.counter >= 5 and self.counter!=9 :
            if self.brd[1] == self.brd[2] == self.brd[3] != ' ': # Checking the top row #Afterwards had to add not equal to blankspace 
                cwc=Tictactoe()
                cwc.declareWinner(self.turn,self.counter)                             #so that it doesnot declare Player 1 as default winner

            elif self.brd[4] == self.brd[5] == self.brd[6] != ' ': # Checking the middle row 
                cwc=Tictactoe()
                cwc.declareWinner(self.turn,self.counter)

            elif self.brd[7] == self.brd[8] == self.brd[9] != ' ': # Checking the bottom row
                cwc=Tictactoe()
                cwc.declareWinner(self.turn,self.counter)

            elif self.brd[1] == self.brd[4] == self.brd[7] != ' ': # Checking the left column
                cwc=Tictactoe()
                cwc.declareWinner(self.turn,self.counter)

            elif self.brd[2] == self.brd[5] == self.brd[8] != ' ': # Checking the middle column
                cwc=Tictactoe()
                cwc.declareWinner(self.turn,self.counter)

            elif self.brd[3] == self.brd[6] == self.brd[9] != ' ': # down the right column
                cwc=Tictactoe()
                cwc.declareWinner(self.turn,self.counter)

            elif self.brd[7] == self.brd[5] == self.brd[3] != ' ': # diagonal 1
                cwc=Tictactoe()
                cwc.declareWinner(self.turn,self.counter)

            elif self.brd[1] == self.brd[5] == self.brd[9] != ' ': # diagonal 2
                cwc=Tictactoe()
                cwc.declareWinner(self.turn,self.counter) 

            

    def askForReplays(self):
            replay = input("\n\n Do you want a rematch??(If yes type Y else type anything else to discontinue....)")
            if replay == "y" or replay == "Y":  
                self.rulebook()
            

    def declareWinner(self,turn,counter):
        print("\nThe Winner is " + turn)
        print("\nGameOver in "+ counter + "moves!!!")
        self.askForReplays()

    def declareDraw(self):
        print("\nThe Game is drawn\n")
        print("\nGameOver!!!")
        self.askForReplays()

    def Startgame(self):
        print("Tic-tac-toe is a two player game.\nPlayer one is '0' and Player 2 is 'X'")
        print(" The objective is to satisfy one of the defined Winning condition...")
        print("Coordinates are as follows:\n")
        print('1' + "  |  "+ '2' + "  |  "+ '3')
        print("--------------")
        print('4' + "  |  "+ '5' + "  |  "+ '6')
        print("--------------")
        print('7' + "  |  "+ '8' + "  |  "+ '9')
        self.gameplay()
    
    def print_board(self,board):
        print(board[1] + '|' + board[2] + '|' + board[3])
        print('-+-+-')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-+-+-')
        print(board[7] + '|' + board[8] + '|' + board[9])


def main():
    ttt = Tictactoe()
    ttt.rulebook()
if __name__ == "__main__":
        main()