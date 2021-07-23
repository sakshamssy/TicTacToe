from array import *

class Players():
    def __init__(self):
        pass

   
    v1=list([])             #these are 2d arrays for storing X or O
    v2=list([])
    v3=list([])
    v4=list([])
    v5=list([])
    v6=list([])
    v7=list([])
    v8=list([])
    v9=list([])



    board=list(['-','O','O','X','X','O','X','O','O','O']) 
    def create_X(self):
        x = [['|','x','x',' ',' ',' ',' ',' ',' ','x', 'x','|'],     #Having a method for creating X
            ['|',' ',' ','x','x',' ',' ','x','x',' ', ' ','|'],
            ['|',' ',' ',' ',' ','x','x',' ',' ',' ', ' ','|'],
            ['|',' ',' ','x','x',' ',' ','x','x',' ', ' ','|'],
            ['|','x','x',' ',' ',' ',' ',' ',' ','x', 'x','|']]
        return(x)

    def create_O(self):
        o=[['|',' ',' ',' ','o','o','o','o',' ',' ', ' ','|'],         #Having a method for creating O
            ['|',' ','o','o',' ',' ',' ',' ','o','o', ' ','|'],
            ['|','o','o',' ',' ',' ',' ',' ',' ','o', 'o','|'],
            ['|',' ','o','o',' ',' ',' ',' ','o','o', ' ','|'],
            ['|',' ',' ',' ','o','o','o','o',' ',' ', ' ','|']]

        return(o)

    def create_empty_list(self):
        e=[['|',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ','|'],         #Having a method for creating emptyspaces
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ','|']]

        return(e)



    def printinfo(self,board):
        if (board[1] =='X'):
            self.v1=self.create_X()                                     #We have stored our choices in brd which we try to copy in v1,v2......
        elif (board[1] =='O'):                                                  #as 2-d arrays of X and O
            self.v1=self.create_O()
        else:
            self.v1=self.create_empty_list()

        if (board[2] =='X'):
            self.v2=self.create_X() 
        elif (board[2] =='O'):
            self.v2=self.create_O()
        else:
            self.v2=self.create_empty_list()
        
        if (board[3] =='X'):
            self.v3=self.create_X() 
        elif (board[3] =='O'):
            self.v3=self.create_O()
        else:
            self.v3=self.create_empty_list()

        if (board[4] =='X'):
            self.v4=self.create_X() 
        elif (board[4] =='O'):
            self.v4=self.create_O()
        else:
            self.v4=self.create_empty_list()

        if (board[5] =='X'):
            self.v5=self.create_X() 
        elif (board[5] =='O'):
            self.v5=self.create_O()
        else:
            self.v5=self.create_empty_list()

        if (board[6] =='X'):
            self.v6=self.create_X() 
        elif (board[6] =='O'):
            self.v6=self.create_O()
        else:
            self.v6=self.create_empty_list()

        if (board[7] =='X'):
            self.v7=self.create_X() 
        elif (board[7] =='O'):
            self.v7=self.create_O()
        else:
            self.v7=self.create_empty_list()

        if (board[8] =='X'):
            self.v8=self.create_X() 
        elif (board[8] =='O'):
            self.v8=self.create_O()
        else:
            self.v8=self.create_empty_list()

        if (board[9] =='X'):
            self.v9=self.create_X() 
        elif (board[9] =='O'):
            self.v9=self.create_O()
        else:
            self.v9=self.create_empty_list()

       
        row_1=[[self.v1,self.v2,self.v3]]             #these v1,v2.. are arranged in 3 
        row_2=[[self.v4,self.v5,self.v6]]
        row_3=[[self.v7,self.v8,self.v9]]



        
        for j in range(0,5):
            for k in range(0,12):
                print(row_1[0][0][j][k],end="")
            for k in range(0,12):
                print(row_1[0][1][j][k],end="")
            for k in range(0,12):
                print(row_1[0][2][j][k],end="")
            print("\n")
        print('-'*36)

        
        for j in range(0,5):
            for k in range(0,12):
                print(row_2[0][0][j][k],end="")
            for k in range(0,12):
                print(row_2[0][1][j][k],end="")
            for k in range(0,12):
                print(row_2[0][2][j][k],end="")
            print("\n")
        print('-'*36)

        
        for j in range(0,5):
            for k in range(0,12):
                print(row_3[0][0][j][k],end="")
            for k in range(0,12):
                print(row_3[0][1][j][k],end="")
            for k in range(0,12):
                print(row_3[0][2][j][k],end="")
            print("\n")

# def main():
#     pp = Players()
#     pp.printinfo(pp.board)

# if __name__ == "__main__":
#     main()



