from board import chessboard
from game import  game
import  random
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
        p2=0
        game(b,rulewin,p1,p2)

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
