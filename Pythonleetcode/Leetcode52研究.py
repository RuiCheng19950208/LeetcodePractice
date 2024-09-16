def queen(A, a,cur=0):

    if cur == len(A):
        a=a+1
        print(a)


        print(A)

        return a
    for col in range(len(A)):
        A[cur], flag = col, True

        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A,a, cur+1)
queen([None]*4,0)