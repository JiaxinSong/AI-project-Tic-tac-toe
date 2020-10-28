
import random
import numpy as np
from judge import judgedraw
from judge import judgerow
from judge import judgecol
from judge import judgediag1
from judge import judgediag2

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