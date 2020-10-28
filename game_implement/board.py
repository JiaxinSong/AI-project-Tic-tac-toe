import numpy as np

#Here is your rule modification: At the end of each turn,
# there is a 25% chance that the other player's turn gets skipped and the current player gets to go again.
class chessboard:
    def __init__(self,size):
        self.boardsize=size
        self.boardstate= np.zeros((2,size, size))
    def printboard(self):

        a=self.boardstate[0]

        b=self.boardstate[1]

        # c=a

        # for i in range(self.boardsize):
        #     for j in range(self.boardsize):
        #         if b[i,j]==1:
        #             c[i,j]=-1

      #  pb=np.full((self.boardsize,self.boardsize),"-","str")

        pd=""

        # for i in range(self.boardsize):
        #     for j in range(self.boardsize):
        #         if a[i][j]==1:
        #             pb[i][j]="o"
        #         if b[i][j] == 1:
        #             pb[i][j] = "x"

        for i in range(self.boardsize):
            for j in range(self.boardsize):
                if a[i][j]==1:
                    pd+="o "
                if b[i][j] == 1:
                    pd+= "x "
                if a[i][j]==0 and  b[i][j]==0 :
                    pd +="+ "
            pd+="\n"
        print(pd)
