class Solution(object):
    def candy(self, ratings):
        n=len(ratings)
        if n==0:
            return 0
        candy=[0]*n
        for i in range(n):
            if i==0:
                candy[i]=1
            elif ratings[i]<=ratings[i-1]:
                candy[i]=1
            else:candy[i]=candy[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]<=ratings[i+1]:
                continue
            elif candy[i]>candy[i+1]:
                continue
            else:
                candy[i]=candy[i+1]+1
                # print(candy)
        return sum(candy)









print(Solution().candy([1,0,2]))
print(Solution().candy([1,2,2]))
print(Solution().candy([1,3,2,2,1]))
print(Solution().candy([1,2,87,87,87,2,1]))

