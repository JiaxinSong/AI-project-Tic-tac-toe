import random
import numpy as np
from board import chessboard
from judge import end_game
from tree_related_functions import AI_action
from tree_related_functions import make_act
import time

def easygame(board, rule,p1):
    b = board.boardstate
    s = board.boardsize
    turns = 0
    nodes = 0

    t = 0
    while True:
        currentstate = b[1] + b[2]
        turns += 1
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
                board.printboard()

                x, y = board.random_play(2)
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

    print("Game Over")
    board.printboard()

def game(board, rule,depth,node, p1):

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

                time_start = time.time()
                act = AI_action(b, 1, rule, depth, node)
                time_end = time.time()
                print('time cost', time_end - time_start, 's')
                x, y = act[0][1]
                print("score:" + str(act[0][0]))
                nodes += act[1]

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

                time_start = time.time()
                act = AI_action(b, 2, rule, depth, node)
                time_end = time.time()
                print('time cost', time_end - time_start, 's')
                x, y = act[0][1]
                print("score:"+str(act[0][0]))
                nodes += act[1]

                make_act(b, 2, x, y)

                print("x:" + str(x))
                print("y:" + str(y))
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