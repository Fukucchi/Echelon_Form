import numpy as np
import sympy as sym


def row_echelon(A):
    """ Return Row Echelon Form of matrix A """

    # if matrix A has no columns or rows,
    # it is already in REF, so we return itself
    # global cnt
    r, c = A.shape
    # print(np.vstack([A[:1], np.hstack([A[1:, :1], B])]))
    if r == 0 or c == 0:
        return A

    # print(A[:,1:])
    # we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i, 0] != 0:
            break
            # go to (*)
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        # here we use recursion
        # print(A[:,1:])
        B = row_echelon(A[:, 1:])
        # print(B)
        # print(np.hstack([A[:,:1], B]))
        # and then add the first zero-column back
        # we now get the row echelon. win!
        return np.hstack([A[:, :1], B])
        # print(np.hstack([A[:,:1], B]))

    # (*) we first see whether non-zero element happens in the first row or not
    # if the former, just divide it by itself (go to (***))
    # if the latter, change rows (go to (**)) and divide it by itself(**)

    # (**)if non-zero element happens not in the first row, we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row
        print(A)
        # print('switched rows')

    # (***) we divide the first row by the first element in it
    A[0] = A[0] / A[0, 0]
    # P[cnt] = P[cnt] / P[cnt, cnt]

    # print(A[0])
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    # print(A[1:,0:1])
    A[1:] -= A[0] * A[1:, 0:1]
    # print(P[cnt+1:,cnt:cnt+1])
    # print('上だよ')
    # P[cnt+1:] -= P[cnt] * P[cnt+1:,cnt:cnt+1]

    # print(np.vstack([A[:1], np.hstack([A[1:,:1], C[cnt+1:,cnt+1:]]) ]))

    # print(A)
    # print(A[1:,:1])

    # for
    # print('succeeded in the first column')

    # we perform REF on matrix from second row, from second column
    # recursion
    # cnt+=1
    B = row_echelon(A[1:, 1:])

    # we add first row and first (zero) column, and return
    # print(A[1:,:1])
    # print(np.vstack([A[:1], np.hstack([A[1:,:1], B]) ]))

    # print(A[:1])
    # print(np.hstack([A[1:, :1], B]))
    # add
    # print(np.vstack([C[:1], np.hstack([C[1:,:1], B]) ]))

    # cnt+=1
    return np.vstack([A[:1], np.hstack([A[1:, :1], B])])


cnt = 0


def row_echelon_new(A):
    """ Return Row Echelon Form of matrix A """

    # if matrix A has no columns or rows,
    # it is already in REF, so we return itself
    global cnt
    r, c = A.shape
    # print(np.vstack([A[:1], np.hstack([A[1:, :1], B])]))
    if r == 0 or c == 0:
        return A

    # print(A[:,1:])
    # we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i, 0] != 0:
            break
            # go to (*)
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        # here we use recursion
        # print(A[:,1:])
        B = row_echelon_new(A[:, 1:])
        # print(B)
        # print(np.hstack([A[:,:1], B]))
        # and then add the first zero-column back
        # we now get the row echelon. win!
        return np.hstack([A[:, :1], B])
        # print(np.hstack([A[:,:1], B]))

    # (*) we first see whether non-zero element happens in the first row or not
    # if the former, just divide it by itself (go to (***))
    # if the latter, change rows (go to (**)) and divide it by itself(**)

    # (**)if non-zero element happens not in the first row, we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row
        print(A)
        print('switched rows')

    # (***) we divide the first row by the first element in it
    A[0] = A[0] / A[0, 0]
    P[cnt] = P[cnt] / P[cnt, cnt]

    # print(A[0])
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    # print(A[1:,0:1])
    A[1:] -= A[0] * A[1:, 0:1]
    # print(P[cnt+1:,cnt:cnt+1])
    # print('上だよ')
    P[cnt + 1:] -= P[cnt] * P[cnt + 1:, cnt:cnt + 1]
    print()
    print(P)
    print(f'第{cnt + 1}列を掃き出しました。')
    # print()
    # process=np.vstack([A_result[:cnt+1], np.hstack( [A_result[cnt+1:,:cnt+1], P[cnt+1:,cnt+1:]] ) ])
    # print(process)
    cnt += 1
    B = row_echelon_new(A[1:, 1:])

    # we add first row and first (zero) column, and return
    # print(A[1:,:1])
    # print(np.vstack([A[:1], np.hstack([A[1:,:1], B]) ]))

    # print(A[:1])
    # print(np.hstack([A[1:, :1], B]))
    # add
    # print(np.vstack([C[:1], np.hstack([C[1:,:1], B]) ]))

    cnt += 1
    return np.vstack([A[:1], np.hstack([A[1:, :1], B])])


A = np.array([[1, 1, 2, 1],
              [2, -1, 1, 2],
              [-1, 1, 2, 3],
              [0, 1, -1, 4]], dtype='float')
print(A)
P = np.copy(A)
# r_P, c_P = P.shape
# print(r_P)
# REA=row_echelon(A)
A_result = row_echelon(A)

print('この行列の階段行列を求めます。第１列から順に掃き出していきます。')
row_echelon_new(A)
# print(A_result)
print('これが欲しかった階段行列です。')
