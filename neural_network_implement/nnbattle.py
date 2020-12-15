import torch as tr

import nn as bn

from score import score

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

board_size = 3
net = bn.NN(board_size)
net.load_state_dict(tr.load("model%d.pth" % board_size))


def nn_puct(board):
    with tr.no_grad():
        x = tr.stack(tuple(map(encode, [b for b in board])))
        y = net(x)
        # probs = tr.softmax(y.flatten(), dim=0)
        # a = np.random.choice(len(probs), p=probs.detach().numpy())

    return y


import random
import numpy as np
from board import chessboard
from judge import end_game
import matplotlib.pyplot as plt

from tree_related_functions import AI_action
from tree_related_functions import make_act
import time


def fig_turns(data):
    plt.hist(data, bins=[i for i in range(30)], color='steelblue', edgecolor='none')
    plt.xlabel("Turns")
    plt.ylabel("Occurrence number")
    plt.title("Occurrence number of turns in 100 games(AI win)")

    plt.savefig("barChart2.jpg")
    plt.show()


def fig_eff(Y, c):
    X = [i for i in range(1,101)]

    plt.bar(X, Y, color=c, width=1.0)

    plt.xlabel("Games")
    plt.ylabel("Number of pieces winner used")
    plt.title("efficiency and performance")

    plt.savefig("barChart51.jpg")

    plt.show()


def game1(board, rule, p1):
    b = board.boardstate

    t = 0
    while True:

        if t == 0:

            if p1 == 1:
                print("Your turn:")
            else:
                print("Opponent turn:")

            x, y = board.random_play(1)

            res = end_game(b, 1, x, y, rule)
            if res == 1:
                print("o win")
                board.printboard()
                return res
            elif res == 0:
                print("draw")
                board.printboard()
                return res

            jump = random.randint(0, 99)
            if (jump <= 24):
                print("Turn gets skipped")
                print()
                t = 0
                continue

        if t == 1:

            if p1 == 1:
                print("Opponent turn:")
            else:
                print("Your turn:")

            board.printboard()

            # print(AI_action(b, 2, rule, 3))
            x, y = board.random_play(2)

            res = end_game(b, 2, x, y, rule)
            if res == 2:
                print("x win")
                board.printboard()
                return res
            elif res == 0:
                print("draw")
                board.printboard()
                return res

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


def game2(board, rule, depth, node, p1):
    b = board.boardstate
    turns = 0
    nodes = 0
    pieces=0
    t = 0
    while True:
        turns += 1
        if t == 0:

            if p1 == 1:
                print("Your turn:")
            else:
                print("Opponent turn:")

            board.printboard()


            lis = list(zip(*np.nonzero(b[0] == 1)))
            bos = []
            resultlist=[]
            for l in lis:
                bcopy = b.copy()
                xx, yy = l

                make_act(bcopy, 1, xx, yy)
                mat = bcopy[1] - bcopy[2]
                END=end_game(bcopy, 1, xx, yy, rule)
                if END==1:
                    resultlist.append(-1)
                elif END==0:
                    resultlist.append(0)
                else:
                    resultlist.append(-score(mat,rule))
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
                    nnp[i][0]+=resultlist[i]

                nnnp = nnp.argmin(dim=0)

                # act = AI_action(b, 2, rule, depth, node)

                x, y = lis[nnnp[0]]

            # nodes+=act[1]

            make_act(b, 1, x, y)

            print("x:" + str(x))
            print("y:" + str(y))

            res = end_game(b, 1, x, y, rule)
            if res == 1:
                print("o win")
                board.printboard()
                pieces=np.sum(b[1])

                return res, turns, pieces
            elif res == 0:
                print("draw")
                board.printboard()
                board.printboard()
                pieces = np.sum(b[1])

                return res, turns, pieces

            jump = random.randint(0, 99)
            if (jump <= 24):
                print("Turn gets skipped")
                print()
                t = 0
                continue

        if t == 1:

            if p1 == 1:
                print("Opponent turn:")
            else:
                print("Your turn:")

            board.printboard()

            act = AI_action(b, 2, rule, depth, node)

            x, y = act[0][1]

            nodes += act[1]

            make_act(b, 2, x, y)

            print("x:" + str(x))
            print("y:" + str(y))

            res = end_game(b, 2, x, y, rule)
            if res == 2:
                print("x win")
                board.printboard()
                pieces = np.sum(b[2])

                return res, turns, pieces
            elif res == 0:
                print("draw")
                board.printboard()
                pieces = np.sum(b[2])

                return res, turns, pieces

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


def game3(board, rule, depth, node, p1):
    b = board.boardstate
    turns = 0
    nodes = 0

    t = 0
    while True:
        turns += 1
        if t == 0:

            if p1 == 1:
                print("Your turn:")
            else:
                print("Opponent turn:")

            board.printboard()

            act = AI_action(b, 1, rule, depth, node)

            x, y = act[0][1]

            nodes += act[1]

            make_act(b, 1, x, y)

            print("x:" + str(x))
            print("y:" + str(y))

            res = end_game(b, 1, x, y, rule)
            if res == 1:
                print("o win")
                board.printboard()
                return res, turns, nodes
            elif res == 0:
                print("draw")
                board.printboard()
                return res, turns, nodes

            jump = random.randint(0, 99)
            if (jump <= 24):
                print("Turn gets skipped")
                print()
                t = 0
                continue

        if t == 1:

            if p1 == 1:
                print("Opponent turn:")
            else:
                print("Your turn:")

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
                if resultlist[ii]==1:
                    x,y=lis[ii]
                    ifwin=1
                    break

            iflose=0
            if ifwin==0:
                for ll in lis:
                    bcopy1 = b.copy()
                    xx1,yy1=ll
                    make_act(bcopy1, 1, xx1, yy1)
                    END = end_game(bcopy1, 1, xx1, yy1, rule)
                    if END == 1:
                        x,y=xx1,yy1
                        iflose=1
                        break

            if iflose==0:
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

            print("x:" + str(x))
            print("y:" + str(y))

            res = end_game(b, 2, x, y, rule)
            if res == 2:
                print("x win")
                board.printboard()
                return res, turns, nodes
            elif res == 0:
                print("draw")
                board.printboard()
                return res, turns, nodes

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


def game4(board, rule, depth, node, p1):
    b = board.boardstate
    turns = 0
    nodes = 0

    t = 0
    while True:
        turns += 1
        if t == 0:

            if p1 == 1:
                print("Your turn:")
            else:
                print("Opponent turn:")

            board.printboard()

            x, y = board.random_play(1)

            res = end_game(b, 1, x, y, rule)
            if res == 1:
                print("o win")
                board.printboard()
                return res, turns, nodes
            elif res == 0:
                print("draw")
                board.printboard()
                return res, turns, nodes

            jump = random.randint(0, 99)
            if (jump <= 24):
                print("Turn gets skipped")
                print()
                t = 0
                continue

        if t == 1:

            if p1 == 1:
                print("Opponent turn:")
            else:
                print("Your turn:")

            board.printboard()

            lis = list(zip(*np.nonzero(b[0] == 1)))
            bos = []
            for l in lis:
                bcopy = b.copy()
                x, y = l
                make_act(bcopy, 2, x, y)
                mat = bcopy[1] - bcopy[2]
                bos.append(mat)

            # print(bos)

            # print(nn_puct(bos))

            nnp = nn_puct(bos)
            nnnp = nnp.argmax(dim=0)
            print(nnp)
            print(nnnp)
            print(lis[nnnp[0]])

            # act = AI_action(b, 2, rule, depth, node)

            x, y = lis[nnnp[0]]

            # nodes+=act[1]

            make_act(b, 2, x, y)

            print("x:" + str(x))
            print("y:" + str(y))

            res = end_game(b, 2, x, y, rule)
            if res == 2:
                print("x win")
                board.printboard()
                return res, turns, nodes
            elif res == 0:
                print("draw")
                board.printboard()
                return res, turns, nodes

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


if __name__ == "__main__":
    xwin = 0
    owin = 0
    draw = 0

    PIECES = []
    TURNS = []
    COLOR = []

    for i in range(100):

        c = chessboard(3)
        time_start = time.time()

        res, turns, pieces = game2(c, 3, 3, 15, 2)  # tree-based+NN AI play at first (board, rule,depth,node, p1)
        # res, turns, nodes = game3(c, 8, 3, 9, 1)     #   tree-based+NN AI play at second

        print('turns',turns)
        print('pieces',pieces)
        PIECES .append(pieces)

        time_end = time.time()
        print('time cost', time_end - time_start, 's')
        if res == 1:
            owin += 1
            COLOR.append("orange")
            print("o win:" + str(owin))
            print("x win:" + str(xwin))
            print("draw:" + str(draw))


        elif res == 2:
            xwin += 1
            COLOR.append("lightskyblue")
            TURNS.append(turns)
            print("o win:" + str(owin))
            print("x win:" + str(xwin))
            print("draw:" + str(draw))
        else:
            draw += 1
            COLOR.append("lightgreen")
            print("o win:" + str(owin))
            print("x win:" + str(xwin))
            print("draw:" + str(draw))

    print()
    print("o win:" + str(owin))
    print("x win:" + str(xwin))
    print("draw:" + str(draw))

    # print(NODES)
    print(COLOR)
    print(TURNS)
    fig_eff(PIECES, COLOR)
    # fig_turns(TURNS)
