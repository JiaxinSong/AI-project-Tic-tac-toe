import random
import numpy as np
from board import chessboard
from judge import end_game
import matplotlib.pyplot as plt

from tree_related_functions import AI_action
from tree_related_functions import make_act
import time

def fig_turns(data):
    plt.hist(data, bins=[i for i in range(110)], color='steelblue', edgecolor='none')
    plt.xlabel("Turns")
    plt.ylabel("Occurrence number")
    plt.title("Occurrence number of turns in 100 games(AI win)")

    plt.savefig("barChart2.jpg")
    plt.show()

def fig_eff(Y,c):
    X=[i for i in range(1,101)]
    plt.bar(X, Y, color=c,width=1.0)
    plt.xlabel("Games")
    plt.ylabel("Number of tree nodes processed")
    plt.title("efficiency and performance")

    plt.savefig("barChart1.jpg")
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

            board.printboard()

            x, y = board.random_play(1)


            res=end_game(b, 1, x, y, rule)
            if res==1:
                print("o win")
                board.printboard()
                return res
            elif res==0:
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

def game2(board, rule,depth,node, p1):

    b = board.boardstate
    turns=0
    nodes=0

    t = 0
    while True:
        turns+=1
        if t == 0:

            if p1 == 1:
                print("Your turn:")
            else:
                print("Opponent turn:")

            board.printboard()


            x, y = board.random_play(1)


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
            else:
                print("Your turn:")

            board.printboard()

            act = AI_action(b, 2, rule, depth, node)

            x, y = act[0][1]

            nodes+=act[1]

            make_act(b, 2, x, y)

            print("x:" + str(x))
            print("y:" + str(y))


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

def game3(board, rule,depth,node, p1):

    b = board.boardstate
    turns=0
    nodes=0

    t = 0
    while True:
        turns+=1
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
            else:
                print("Your turn:")

            board.printboard()

            x, y = board.random_play(2)

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

if __name__ == "__main__":
    xwin=0
    owin=0
    draw=0


    for i in range(100):
        b = chessboard(7)
        res=game1(b,5,1)
        if res==1:
            owin+=1
        elif res==2:
            xwin+=1
        else: draw+=1

    print("o win:" + str(owin))
    print("x win:" + str(xwin))
    print("draw:" + str(draw))

    print()






    xwin = 0
    owin = 0
    draw = 0

    NODES=[]
    TURNS=[]
    COLOR=[]

    for i in range(100):



        c = chessboard(10)
        time_start = time.time()


        res,turns,nodes = game2(c, 8, 3, 9, 2)         #tree-based AI play at second
        #res, turns, nodes = game3(c, 8, 3, 9, 1)     #   tree-based AI play at first


        print(turns)
        print(nodes)
        NODES.append(nodes)



        time_end = time.time()
        print('time cost', time_end - time_start, 's')
        if res==1:
            owin+=1
            COLOR.append("orange")
            print("o win:" + str(owin))
            print("x win:" + str(xwin))
            print("draw:" + str(draw))
        elif res==2:
            xwin+=1
            COLOR.append("lightskyblue")
            TURNS.append(turns)
            print("o win:" + str(owin))
            print("x win:" + str(xwin))
            print("draw:" + str(draw))
        else:
            draw+=1
            COLOR.append("lightgreen")
            print("o win:" + str(owin))
            print("x win:" + str(xwin))
            print("draw:" + str(draw))

    print()
    print("o win:"+str(owin))
    print("x win:"+str(xwin))
    print("draw:"+str(draw))

    print(NODES)
    print(COLOR)
    print(TURNS)
    fig_eff(NODES,COLOR)
    fig_turns(TURNS)



