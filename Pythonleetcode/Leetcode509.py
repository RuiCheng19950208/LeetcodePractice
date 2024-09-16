class Solution(object):
    def fib(self, N):
        if N==0:
            return 0
        if N<=2:
            return 1
        F=[0]*N
        F[0]=1
        F[1] = 1
        for i in range(2,N):
            F[i]=F[i-1]+F[i-2]
        return F[-1]



print(Solution().fib(3))
print(Solution().fib(4))