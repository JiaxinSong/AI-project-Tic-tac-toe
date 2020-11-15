import numpy as np
import random
from score import score
from judge import end_game


def valid_actions1(board):
    return list(zip(*np.nonzero(board[0] == 1)))


def exminimax(board, d, rule, action, depth, node, l):  # action = (x,y)
    l.append(1)
    e, f = action
    end = end_game(board, d, e, f, rule)
    if end == d:  # d win
        if d == 1:
            return 1 * (depth + 1)
        else:
            return -1 * (depth + 1)
    elif end == 0:  # draw

        return 0

    else:
        if depth == 0:

            matrix = board[1] - board[2]
            # print(matrix)
            return score(matrix, rule)

        else:

            if d == 1:
                a = 1
                b = 2
            else:
                a = 2
                b = 1

            child_utilities1 = []
            child_utilities2 = []

            va=valid_actions1(board)   #valid_action

            len_va=len(va)

            if len_va>node:
                ca= random.sample(va,node) #choose_action
                # print(len(ca))
                # print(ca)
            else:
                ca=random.sample(va,len_va)
                # print(ca)


            for i in ca:
                # print(i)

                x, y = i
                make_act(board, b, x, y)
                child_utilities1.append(exminimax(board, b, rule, i, depth - 1,node, l))
                recover_act(board, b, x, y)


                make_act(board, a, x, y)
                child_utilities2.append(exminimax(board, a, rule, i, depth - 1, node,l))
                recover_act(board, a, x, y)
            # print()
            if d == 1:
                # print(min(child_utilities1),max(child_utilities2))
                return 0.75 * min(child_utilities1) + 0.25 * max(child_utilities2)
            else:
                # print(max(child_utilities1),min(child_utilities2))
                return 0.75 * max(child_utilities1) + 0.25 * min(child_utilities2)



# AI

def make_act(board, d, x, y):  # this board is a matrix
    board[0][x][y] = 0
    board[d][x][y] = 1


def recover_act(board, d, x, y):
    board[0][x][y] = 1
    board[d][x][y] = 0


def AI_action(board, d, rule, depth,node):  # return ((score,position),nodes)

    newboard = board.copy()
    res = []

    l = []
    print("valid_actions: "+str(len(valid_actions1(newboard))))
    for i in valid_actions1(board):

        newboard = board.copy()
        x, y = i
        make_act(newboard, d, x, y)

        nscore = exminimax(newboard, d, rule, i, depth - 1, node,l)

        res.append((nscore, i))

    print("Node searched: "+str(len(l)))

    if d == 1:
        maxres = max(res)

        return maxres,len(l)

    else:
        minres = min(res)

        return minres,len(l)
