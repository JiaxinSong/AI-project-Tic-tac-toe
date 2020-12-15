import numpy as np

def score(matrix,rule):          #matrix  : 0 1 -1
    size = matrix.shape[0]
    max1=0
    max2=0

    a1,a2=max_row(matrix,rule)
    b1,b2=max_col(matrix,rule)
    c1,c2=max_dig1(matrix,rule)
    d1,d2=max_dig2(matrix,rule)

    max1=max(a1,b1,c1,d1)
    max2=max(a2,b2,c2,d2)

    if max1>max2:
        return 0.5
    elif max1<max2:
        return  -0.5
    else :
        return 0


def max_row(matrix, rule):  # matrix : n x n     element:0 1 -1
    size = matrix.shape[0]
    maxr1 = 0
    maxr2 = 0
    for i in range(size):
        maxr1 = max(together_row(matrix[i], 1, rule), maxr1)
        maxr2 = max(together_row(matrix[i], 2, rule), maxr2)

    return maxr1,maxr2



def max_col(matrix, rule):
    matrix = np.rot90(matrix, 1)
    size = matrix.shape[0]
    maxr1 = 0
    maxr2 = 0
    for i in range(size):
        maxr1 = max(together_row(matrix[i], 1, rule), maxr1)
        maxr2 = max(together_row(matrix[i], 2, rule), maxr2)

    return maxr1,maxr2


def max_dig1(matrix,rule):
    size = matrix.shape[0]
    maxr1 = 0
    maxr2 = 0
    for i in range(-size+ 1,size):
        if len(np.diagonal(matrix,offset=i))>=rule:
            maxr1 = max(together_row(np.diagonal(matrix,offset=i),1,rule),maxr1)
            maxr2 = max(together_row(np.diagonal(matrix, offset=i), 2, rule), maxr2)

    return maxr1,maxr2

def max_dig2(matrix,rule):
    matrix = np.rot90(matrix, 1)
    size = matrix.shape[0]
    maxr1 = 0
    maxr2 = 0
    for i in range(-size + 1, size):
        if len(np.diagonal(matrix, offset=i)) >= rule:
            maxr1 = max(together_row(np.diagonal(matrix, offset=i), 1, rule), maxr1)
            maxr2 = max(together_row(np.diagonal(matrix, offset=i), 2, rule), maxr2)

    return maxr1, maxr2



# input [1,2,3,4]
def together_row(vec, d, rule):  # valid consecutive piece in a singe row
    size = vec.shape[0]

    max_to = 0  # max together
    ct = 0  # current together pieces
    mct = 0  # current max together

    slow = 0

    if d == 1:
        for i in range(size):
            if i == 0:
                if vec[i] == 1:
                    ct = ct + 1
                    mct = ct

                if vec[i] == -1:
                    slow = i + 1
                    ct = 0
                    mct = 0
            else:
                if vec[i] == 1:
                    if vec[i - 1] == 1:
                        ct = ct + 1
                        mct = max(ct, mct)

                    if vec[i - 1] == -1:
                        slow = i
                        ct = ct + 1
                        mct = max(ct, mct)

                    if vec[i - 1] == 0:
                        ct = 1
                        mct = max(ct, mct)

                if vec[i] == -1:
                    slow = i + 1
                    ct = 0
                    mct = 0

                if vec[i] == 0:
                    ct = 0
                    mct = max(ct, mct)

            if i - slow + 1 >= rule:
                max_to = max(max_to, mct)

    if d == 2:
        for i in range(size):
            if i == 0:
                if vec[i] == -1:
                    ct = ct + 1
                    mct = ct

                if vec[i] == 1:
                    slow = i + 1
                    ct = 0
                    mct = 0
            else:
                if vec[i] == -1:
                    if vec[i - 1] == -1:
                        ct = ct + 1
                        mct = max(ct, mct)

                    if vec[i - 1] == 1:
                        slow = i
                        ct = ct + 1
                        mct = max(ct, mct)

                    if vec[i - 1] == 0:
                        ct = 1
                        mct = max(ct, mct)

                if vec[i] == 1:
                    slow = i + 1
                    ct = 0
                    mct = 0

                if vec[i] == 0:
                    ct = 0
                    mct = max(ct, mct)

            if i - slow + 1 >= rule:
                max_to = max(max_to, mct)

    return max_to



if __name__ == "__main__":
    a= np.array([[1., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [-1., 0., 0., -1., 0.],
        [0., 0., 0., 0, 0.]])
    print(score(a,3))
#     p = np.array([0, -1, -1, 0, -1, -1, -1, 0, -1, 1, 1, 1, 0, -1])
#
#     # for i in range(0,11):
#     #     print(together_row(p[::-1], 1, i))
#     #     print(together_row(p, 1, i))
#     #     print()
#
#     p = np.array([[1, -1, -1, -1, -1],
#                   [ -1, -1, 0, 1, 0],
#                   [ -1, 1, 1, -1,1],
#                   [ 1, 1, 0, -1,1],
#                   [ 1, 1, 0, -1,1]])
#
#     x = np.array([[0, -1, -1, 0],
#                   [-1, -1, 0, -1],
#                   [0, 1, 0, -1],
#                   [1, 1, 0, -1]])
#
#
#     print(p)
#     print(max_col(p,3))
#     print(max_row(p,3))
#
#
#
#     print(max_dig2(p,3))
#
#     print(max_dig1(p, 3))
#
#     print(max_dig2(x, 3))
#     print(max_dig2(x, 3)[0])
#     print(max_dig2(x, 3)[1])
#
#
#     print()
#
#     print(score(p,3))







