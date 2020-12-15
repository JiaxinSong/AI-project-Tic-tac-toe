import random
import numpy as np

from board import chessboard
from judge import end_game
from tree_related_functions import AI_action
from tree_related_functions import make_act
import time
from judge import judgedraw
from judge import judgerow
from judge import judgecol
from judge import judgediag1
from judge import judgediag2
from score import score

import torch as tr
import nn as bn

def encode(board):
    matrix = tr.zeros(3, len(board), len(board))

    pos = [(x, y) for x in range(len(board)) for y in range(len(board))]
    for (r, c) in pos:
        if board[r, c] == 0:
            matrix[0, r, c] = 1
        elif board[r, c] == 1:
            matrix[1, r, c] = 1
        elif board[r, c] == -1:
            matrix[2, r, c] = 1
    return matrix


board_size = 5
net = bn.NN(board_size)
net.load_state_dict(tr.load("model%d.pth" % board_size))

def nn_puct(board):
    with tr.no_grad():
        x = tr.stack(tuple(map(encode, [b for b in board])))
        y = net(x)
        # probs = tr.softmax(y.flatten(), dim=0)
        # a = np.random.choice(len(probs), p=probs.detach().numpy())

    return y


def gamenn3(board, rule ,p1):

    b = board.boardstate
    s = board.boardsize
    turns=0
    nodes=0

    t = 0
    while True:
        currentstate = b[1] + b[2]
        turns+=1
        if t == 0:

            if p1 == 1:
                print("Your turn:")
                board.printboard()
                while True:
                    print("Please put piece to make it in a suitable position.")
                    x = input("x-axis coordinate:")
                    y = input("y-axis coordinate:")
                    if (x.isdecimal() and y.isdecimal() and int(x) >= 0 and int(x) < s and int(y) >= 0 and int(
                            y) < s and currentstate[int(x)][int(y)] != 1):
                        break
                    print("Impossible position!")

                print()
                x = int(x)
                y = int(y)
                make_act(b, 1, x, y)

            else:
                print("Opponent turn:")
                board.printboard()

                lis = list(zip(*np.nonzero(b[0] == 1)))
                bos = []
                resultlist = []
                for l in lis:
                    bcopy = b.copy()
                    xx, yy = l

                    make_act(bcopy, 1, xx, yy)
                    mat = bcopy[1] - bcopy[2]
                    END = end_game(bcopy, 1, xx, yy, rule)
                    if END == 1:
                        resultlist.append(-1)
                    elif END == 0:
                        resultlist.append(0)
                    else:
                        resultlist.append(-score(mat, rule))
                    bos.append(mat)

                ifwin = 0
                for ii in range(len(resultlist)):
                    if resultlist[ii] == -1:
                        x, y = lis[ii]
                        ifwin = 1
                        break

                iflose = 0
                if ifwin == 0:
                    for ll in lis:
                        bcopy1 = b.copy()
                        xx1, yy1 = ll
                        make_act(bcopy1, 2, xx1, yy1)
                        END = end_game(bcopy1, 2, xx1, yy1, rule)
                        if END == 2:
                            x, y = xx1, yy1
                            iflose = 1
                            break

                # print(bos)

                # print(nn_puct(bos))
                if iflose == 0:
                    nnp = nn_puct(bos)
                    for i in range(len(resultlist)):
                        nnp[i][0] += resultlist[i]

                    nnnp = nnp.argmin(dim=0)

                    # act = AI_action(b, 2, rule, depth, node)

                    x, y = lis[nnnp[0]]

                # nodes+=act[1]

                make_act(b, 1, x, y)

                print("x:" + str(x))
                print("y:" + str(y))
                print()

            res=end_game(b, 1, x, y, rule)
            if res==1:
                print("o win")
                board.printboard()
                return res,turns,nodes
            elif res==0:
                print("draw")
                board.printboard()
                return res,turns,nodes


            jump = random.randint(0, 99)
            if (jump <= 24):
                print("Turn gets skipped")
                print()
                t = 0
                continue

        if t == 1:

            if p1 == 1:
                print("Opponent turn:")
                board.printboard()

                lis = list(zip(*np.nonzero(b[0] == 1)))
                bos = []
                resultlist = []

                for l in lis:
                    bcopy = b.copy()
                    xx, yy = l
                    make_act(bcopy, 2, xx, yy)
                    mat = bcopy[1] - bcopy[2]
                    END = end_game(bcopy, 2, xx, yy, rule)
                    if END == 2:
                        resultlist.append(1)
                    elif END == 0:
                        resultlist.append(0)
                    else:
                        resultlist.append(-score(mat, rule))
                    bos.append(mat)

                ifwin = 0
                for ii in range(len(resultlist)):
                    if resultlist[ii] == 1:
                        x, y = lis[ii]
                        ifwin = 1
                        break

                iflose = 0
                if ifwin == 0:
                    for ll in lis:
                        bcopy1 = b.copy()
                        xx1, yy1 = ll
                        make_act(bcopy1, 1, xx1, yy1)
                        END = end_game(bcopy1, 1, xx1, yy1, rule)
                        if END == 1:
                            x, y = xx1, yy1
                            iflose = 1
                            break

                if iflose == 0:
                    # print(bos)

                    # print(nn_puct(bos))
                    #     print(resultlist)

                    nnp = nn_puct(bos)
                    # print(nnp)
                    for i in range(len(resultlist)):
                        nnp[i][0] += resultlist[i]
                    # print(nnp)
                    nnnp = nnp.argmax(dim=0)

                    x, y = lis[nnnp[0]]

                # nodes+=act[1]

                make_act(b, 2, x, y)
                print()
            else:

                print("Your turn:")
                board.printboard()
                while True:
                    print("Please put piece to make it in a suitable position.")
                    x = input("x-axis coordinate:")
                    y = input("y-axis coordinate:")
                    if (x.isdecimal() and y.isdecimal() and int(x) >= 0 and int(x) < s and int(y) >= 0 and int(
                            y) < s and currentstate[int(x)][int(y)] != 1):
                        break
                    print("Impossible position!")

                print()
                x = int(x)
                y = int(y)
                make_act(b, 2, x, y)


            res = end_game(b, 2, x, y, rule)
            if res == 2:
                print("x win")
                board.printboard()
                return res,turns,nodes
            elif res == 0:
                print("draw")
                board.printboard()
                return res,turns,nodes

            jump = random.randint(0, 99)

            if (jump <= 24):
                print("Turn gets skipped")
                print()
                t = 1
                continue

        if t == 0:
            t = 1
        else:
            t = 0



    print("Game Over")
    board.printboard()


def game(board,rule,p1,p2):
    p1win=0
    p2win=0
    draw=0
    b=board.boardstate
    s=board.boardsize



    t = 0
    while True:
        currentstate=b[0]+b[1]

        if t==0:


            if p1==1:
                print("Your turn:")
            else:
                print("Opponent turn:")

            board.printboard()

            while True:
                print("Please put piece to make it in a suitable position.")
                x = input("x-axis coordinate:")
                y = input("y-axis coordinate:")
                if (x.isdecimal() and y.isdecimal() and int(x) >= 0 and int(x) < s and int(y) >= 0 and int(y) < s and currentstate[int(x)][int(y)] != 1):
                    break
                print("Impossible position!")

            print()
            x=int(x)
            y=int(y)
            b[0][x][y]=1

#judge row
            p1win=judgerow(b[0],s,p1win,x,y,rule)
            if p1win==1:
                print("o win!")
                break


#judge col
            p1win = judgecol(b[0], s, p1win, x, y, rule)
            if p1win == 1:
                print("o win!")
                break

#judge diagonal 1
            p1win= judgediag1(b[0], s, p1win, x, y, rule)
            if p1win==1:
                print("o win!")
                break

# judge diagonal 2

            p1win = judgediag2(b[0], s, p1win, x, y, rule)
            if p1win == 1:
                print("o win!")
                break

            if judgedraw(b, s, draw) == 1:
                print("Draw!")
                break

            jump = random.randint(0, 99)
            if (jump <= 24):
                print("Turn gets skipped")
                print()
                t = 0
                continue


        if t==1:

            if p1 == 1:
                print("Opponent turn:")
            else:
                print("Your turn:")

            board.printboard()

            while True:
                print("Please put piece to make it in a suitable position.")
                x = input("x-axis coordinate:")
                y = input("y-axis coordinate:")
                if (x.isdecimal() and y.isdecimal() and int(x) >= 0 and int(x) < s and int(y) >= 0 and int(y) < s and
                        currentstate[int(x)][int(y)] != 1):
                    break
                print("Impossible position!")

            x=int(x)
            y=int(y)
            print()

            b[1][x][y] = 1

            # judge row

            p2win = judgerow(b[1], s, p2win, x, y, rule)
            if p2win == 1:
                print("x win!")
                break

            # judge col

            p2win = judgecol(b[1], s, p2win, x, y, rule)
            if p2win == 1:
                print("x win!")
                break

            # judge diagonal 1


            p2win=judgediag1(b[1], s, p2win, x, y, rule)

            if p2win == 1:
                print("x win!")
                break

            # judge diagonal 2


            p2win=judgediag2(b[1], s, p2win, x, y, rule)

            if p2win == 1:
                print("x win!")
                break

            if judgedraw(b, s, draw) == 1:
                print("Draw!")
                break

            jump = random.randint(0, 99)

            if (jump <= 24):
                print("Turn gets skipped")
                print()
                t = 1
                continue



        if t==0:
            t=1
        else:
            t=0


    print("Game Over")
    board.printboard()