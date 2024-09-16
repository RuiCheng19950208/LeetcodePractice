class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        ans=[False]*len(A)
        number=0
        for i in range(len(A)):
            number= number*2+A[i]
            if number%5==0:
                ans[i]=True
        return ans




print(Solution().prefixesDivBy5([0,1,1]))
print(Solution().prefixesDivBy5([1,1,1]))
print(Solution().prefixesDivBy5([0,1,1,1,1,1]))
print(Solution().prefixesDivBy5([1,1,1,0,1]))
