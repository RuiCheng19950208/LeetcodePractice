import copy
class Solution(object):
    def climbStairs(self, n):
        def jiecheng(n):
            if n==0:
                return 1
            m=copy.deepcopy(n)
            while n!=1:
                n=n-1
                m=m*n
            return m


        def zuhe(x,y):
            return jiecheng(y)/(jiecheng(x)*jiecheng(y-x))

        sum=0
        if n%2==0:
            k=int(n/2)

            for i in range(k+1):
                sum=sum+zuhe(2*i,k+i)
            return sum


        else:
            k=int((n-1)/2)
            for i in range(k+1):
                sum=sum+zuhe(2*i+1,k+i+1)
            return int(sum)


print(Solution().climbStairs(7))


