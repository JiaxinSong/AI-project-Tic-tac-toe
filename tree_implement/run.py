from board import chessboard
from game import  game
from game import easygame

if __name__ == "__main__":
    print("Welcome to our game! This is a tictactoe game.")
    print("What's more is that At the end of each turn, there is a 25% chance that the other player's turn gets skipped and the current player gets to go again.")
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
        g = input("Options: 1.VS baseline AI(random player) 2. VS tree-based AI, input 1 or 2: ")

        if g.isdecimal() and (int(g)==1 or int(g)==2):
            break
        else:
            print("Please input a positive integer and it should not exceed the board size.")

    g=int(g)

    if g==2:
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

            game(b,rulewin,depth,nodes,p1)

        else:
            print("Your opponent will go first.")
            print("Your pieces are x")
            print("Your can put your pieces on + ")
            print()
            print("Game begin")
            print()
            p1 = 0

            game(b,rulewin,depth,nodes,p1)

    if g==1:
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

