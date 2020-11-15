import numpy as np

# input [1,2,3,4]
def score_row(vec,rule):
    size=vec.shape[0]

    max_to=0   # max together
    ct=0   # current together pieces

    slow=0
    for i in range(size):
        if i==0:
            if vec[i]==1:
                ct=ct+1

            if vec[i]==-1:
                slow=i+1
                ct=0
        else:
            if vec[i]==1:
                if vec[i-1]==1:
                    ct=ct+1

                if vec[i-1]==-1:
                    slow=i
                    ct=ct+1

                if vec[i-1]==0:
                    ct=1

            if vec[i]==-1:
                slow =i+1
                ct=0

            if vec[i]==0:
                ct=0

        if i-slow+1>=rule:
            max_to=max(max_to,ct)

def end_game(board,d,x,y,rule):     # board       return 0 : draw 1: o win
    size=board[0].shape[0]
    win =0
    draw=0

    if judgerow(board[d],size,win,x,y,rule)==1:
        return d
    if judgecol(board[d],size,win,x,y,rule)==1:
        return d
    if judgediag1(board[d],size,win,x,y,rule)==1:
        return d
    if judgediag2(board[d],size,win,x,y,rule)==1:
        return d

    if judgedraw(board,size,draw)==1:
        return 0

    return -1





def judgedraw(board,size,draw):   # board
    check = board[2] + board[1]
    if check.sum() == size * size:
        draw = 1

    return draw


def judgerow(board,s,win,x,y,rule):    # part of board
    start = y - rule + 1
    if start < 0:
        start = 0

    end = y
    if y + rule - 1 > s - 1:
        end = s - rule

    for i in range(start, end + 1):
        judge1 = True
        for j in range(rule):
            if board[x][i + j] == 0:
                judge1 = False
                break
        if judge1 == True:
            win = 1
    return win

def judgecol(board,s,win,x,y,rule):   # part of board
    start = x - rule + 1
    if start < 0:
        start = 0

    end = x
    if x + rule - 1 > s - 1:
        end = s - rule

    for i in range(start, end + 1):
        judge2 = True
        for j in range(rule):
            if board[i + j][y] == 0:
                judge2 = False
                break
        if judge2 == True:
            win = 1
            break
    return win

def judgediag1(board,s,win,x,y,rule):    # part of board
    if s - abs(x - y) >= rule:
        startx, starty = x, y
        endx, endy = x, y

        while (startx > 0 and starty > 0 and abs(startx - x) < rule - 1):
            startx = startx - 1
            starty = starty - 1

        while (endx < s - 1 and endy < s - 1 and abs(endx - x) < rule - 1):
            endx = endx + 1
            endy = endy + 1

        endx = endx - rule + 1
        endy = endy - rule + 1

        for i in range(startx, endx + 1):
            judge3 = True
            for j in range(rule):
                if board[i + j][i + j - x + y] == 0:
                    judge3 = False
                    break
            if judge3 == True:
                win = 1
                break
        return win

def judgediag2(board,s,win,x,y,rule):    # part of board

    nb = np.rot90(board, 1)

    yy = y
    y = x
    x = s - 1 - yy

    if s - abs(x - y) >= rule:
        startx, starty = x, y
        endx, endy = x, y

        while (startx > 0 and starty > 0 and abs(startx - x) < rule - 1):
            startx = startx - 1
            starty = starty - 1

        while (endx < s - 1 and endy < s - 1 and abs(endx - x) < rule - 1):
            endx = endx + 1
            endy = endy + 1

        endx = endx - rule + 1
        endy = endy - rule + 1

        for i in range(startx, endx + 1):
            judge3 = True
            for j in range(rule):
                if nb[i + j][i + j - x + y] == 0:
                    judge3 = False
                    break
            if judge3 == True:
                win = 1
                break
        return win