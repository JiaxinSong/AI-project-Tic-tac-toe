import numpy as np
def judgedraw(board,size,draw):
    check = board[0] + board[1]
    if check.sum() == size * size:
        draw = 1

    return draw


def judgerow(board,s,win,x,y,rule):
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

def judgecol(board,s,win,x,y,rule):
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

def judgediag1(board,s,win,x,y,rule):
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

def judgediag2(board,s,win,x,y,rule):

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