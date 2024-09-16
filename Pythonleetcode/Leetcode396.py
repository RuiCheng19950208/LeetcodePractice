class Solution(object):
    def maxRotateFunction(self, A):
        if len(A)==1:
            return 0
        len_A = len(A)
        sum_A=sum(A)
        best = sum([i * A[i] for i in range(len_A)])
        n=best+0
        for i in range(1,len_A):
            n=n+sum_A-len_A*A[-i]
            best=max(best,n)
            # print(best,n,A[-i])
        return best

print(Solution().maxRotateFunction([4, 3, 2, 6]))