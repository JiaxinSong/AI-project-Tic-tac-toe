import numpy as np
import random

class chessboard:
    def __init__(self,size):
        self.boardsize=size
        self.boardstate= np.zeros((3,size, size))       #[1]o   [2]x
        self.boardstate[0]=1

    def perform(self, action,d):
        row, col = action
        new_state = self.boardstate.copy()
        new_state.board[d][row][col] = 1
        new_state.board[0][row][col] = 0
        return new_state

    #baseline
    def random_play(self, d):
        b = self.boardstate
        s = self.boardsize

        v=self.valid_actions()

        x,y =random.choice(v)

        print("x:"+str(x))
        print("y:"+str(y))

        self.make_action (d,x,y)

        return x,y

    def randomm(self, d):
        b = self.boardstate
        s = self.boardsize

        v = self.valid_actions()

        x, y = random.choice(v)

        return x, y



    def valid_actions(self):
        return list(zip(*np.nonzero(self.boardstate[0] == 1)))

    def make_action(self,d,x,y):    #d=1 or 0
        self.boardstate[0][x][y]=0
        self.boardstate[d][x][y]=1


    def printboard(self):

        a=self.boardstate[0]

        b=self.boardstate[1]

        c = self.boardstate[2]

        pd=""

        for i in range(self.boardsize):
            for j in range(self.boardsize):
                if b[i][j]==1:
                    pd+="o "
                if c[i][j] == 1:
                    pd+= "x "
                if a[i][j]==1 :
                    pd +="+ "
            pd+="\n"
        print(pd)
