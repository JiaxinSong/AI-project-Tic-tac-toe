from board import chessboard

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







if __name__ == "__main__":
    print("Welcome to our game! This is a tictactoe game.")
    print("What's more is that At the end of each turn, there is a 25% chance that the other player's turn gets skipped and the current player gets to go again.")

    while True:
        nnai = input("There are four kinds of game modes: play with human or baseline AI or tree-based AI or tree+NN-based AI. Do you want to play with tree+NN-based AI?  \nPlease type Y or N: ")
        if nnai == "Y" or nnai == "N":
            break
        else:
            print("Please input Y or N.")

    if nnai=="Y":
        while True:
            choosesizeandrule = input(
                "There are five kinds of games:\n1. board size: 3*3 winning target: 3 \n2. board size: 4*4 winning target: 3 \n3. board size: 5*5 winning target: 3 \n4. board size: 6*6 winning target: 4 \n5. board size: 7*7 winning target: 4 \n"
                "please input number: ")
            if choosesizeandrule.isdecimal() and (int(choosesizeandrule) == 1 or int(choosesizeandrule) == 2 or int(choosesizeandrule) == 3 or int(choosesizeandrule) == 4 or int(choosesizeandrule) == 5):
                break
            else:
                print("Please input a valid number.")

        choosesizeandrule = int(choosesizeandrule)

        if choosesizeandrule==1:
            from game import gamenn1
            b = chessboard(3)

            while True:
                first = input("Do you want to go first?    Please type Y or N:")
                if first == "Y" or first == "N":
                    break
                else:
                    print("Please input Y or N.")

            if first == "Y":
                print("You will go first.")
                print("Your pieces are o")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 1

                gamenn1(b, 3 , p1)

            else:
                print("Your opponent will go first.")
                print("Your pieces are x")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 0

                gamenn1(b, 3 , p1)

        elif choosesizeandrule==2:
            from game2 import gamenn2

            b = chessboard(4)

            while True:
                first = input("Do you want to go first?    Please type Y or N:")
                if first == "Y" or first == "N":
                    break
                else:
                    print("Please input Y or N.")

            if first == "Y":
                print("You will go first.")
                print("Your pieces are o")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 1

                gamenn2(b, 3, p1)

            else:
                print("Your opponent will go first.")
                print("Your pieces are x")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 0

                gamenn2(b, 3, p1)
        #
        elif choosesizeandrule==3:
            from game3 import gamenn3

            b = chessboard(5)

            while True:
                first = input("Do you want to go first?    Please type Y or N:")
                if first == "Y" or first == "N":
                    break
                else:
                    print("Please input Y or N.")

            if first == "Y":
                print("You will go first.")
                print("Your pieces are o")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 1

                gamenn3(b, 3, p1)

            else:
                print("Your opponent will go first.")
                print("Your pieces are x")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 0

                gamenn3(b, 3, p1)

        elif choosesizeandrule==4:
            from game4 import gamenn4

            b = chessboard(6)

            while True:
                first = input("Do you want to go first?    Please type Y or N:")
                if first == "Y" or first == "N":
                    break
                else:
                    print("Please input Y or N.")

            if first == "Y":
                print("You will go first.")
                print("Your pieces are o")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 1

                gamenn4(b, 4, p1)

            else:
                print("Your opponent will go first.")
                print("Your pieces are x")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 0

                gamenn4(b, 4, p1)

        elif choosesizeandrule==5:
            from game5 import gamenn5

            b = chessboard(7)

            while True:
                first = input("Do you want to go first?    Please type Y or N:")
                if first == "Y" or first == "N":
                    break
                else:
                    print("Please input Y or N.")

            if first == "Y":
                print("You will go first.")
                print("Your pieces are o")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 1

                gamenn5(b, 4, p1)

            else:
                print("Your opponent will go first.")
                print("Your pieces are x")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 0

                gamenn5(b, 4, p1)





    elif nnai=="N":
        while True:
            bs = input("Please set the size of board:")
            if bs.isdecimal() and int(bs)>0:
                break
            else:
                print("Please input a positive integer:")
        bs=int(bs)



        while True:
            rulewin = input("How many pieces in the same row, in the same column or in the same diagonal successively "
                            "will win the game?:")

            if rulewin.isdecimal() and int(rulewin)>0 and int(rulewin)<=bs:
                break
            else:
                print("Please input a positive integer and it should not exceed the board size.")

        rulewin=int(rulewin)


        while True:
            g = input("Options: 1.VS baseline AI(random player) 2. VS tree-based AI 3. VS human, input 1 or 2 or 3: ")

            if g.isdecimal() and (int(g)==1 or int(g)==2 or int(g)==3):
                break
            else:
                print("Please input a positive integer and it should not exceed the board size.")

        g=int(g)


        if g==3:
            from game import game
            b = chessboard(bs)

            print()

            print("Boardsize is " + str(bs) + ". Win rule is " + str(rulewin) + ".")

            print()

            while True:
                first = input("Do you want to go first?    Please type Y or N:")
                if first == "Y" or first == "N":
                    break
                else:
                    print("Please input Y or N.")

            if first == "Y":
                print("You will go first.")
                print("Your pieces are o")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 1
                p2 = 0
                game(b, rulewin, p1, p2)

            else:
                print("Your opponent will go first.")
                print("Your pieces are x")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 0
                p2 = 1
                game(b, rulewin, p1, p2)

        if g==2:
            from game import gametree
            while True:
                depth = input("What is the depth of minimax tree you want AI to search each turn?(start with samll number or you may wait for a long time):")

                if depth.isdecimal() and int(depth)>0 :
                    break
                else:
                    print("Please input a positive integer.")
            depth = int(depth)

            while True:
                nodes = input("How many nodes on each layer of minimax tree you want AI to search each turn?(start with samll number or you may wait for a long time) ?:")

                if nodes.isdecimal() and int(nodes)>0:
                    break
                else:
                    print("Please input a positive integer.")

            nodes=int(nodes)

            b=chessboard(bs)

            print()

            print("Boardsize is "+str(bs)+". Win rule is "+str(rulewin)+"." )

            print()

            while True:
                first= input("Do you want to go first?    Please type Y or N:")
                if first=="Y" or first=="N":
                    break
                else:
                    print("Please input Y or N.")


            if first=="Y":
                print("You will go first.")
                print("Your pieces are o")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1=1

                gametree(b,rulewin,depth,nodes,p1)

            else:
                print("Your opponent will go first.")
                print("Your pieces are x")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 0

                gametree(b,rulewin,depth,nodes,p1)

        if g==1:
            from game import easygame
            b = chessboard(bs)

            print()

            print("Boardsize is " + str(bs) + ". Win rule is " + str(rulewin) + ".")

            print()

            while True:
                first = input("Do you want to go first?    Please type Y or N:")
                if first == "Y" or first == "N":
                    break
                else:
                    print("Please input Y or N.")

            if first == "Y":
                print("You will go first.")
                print("Your pieces are o")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 1

                easygame(b, rulewin, p1)

            else:
                print("Your opponent will go first.")
                print("Your pieces are x")
                print("Your can put your pieces on + ")
                print()
                print("Game begin")
                print()
                p1 = 0

                easygame(b, rulewin, p1)

