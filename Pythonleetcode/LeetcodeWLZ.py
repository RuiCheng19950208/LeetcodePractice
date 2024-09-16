class Solution(object):
    def smallestRangeI(self, A):
        ans=[]
        part=[]
        for i in range(len(A)):
            if A[i]>=A[i-1] or len(part)==0:
                part.append(A[i])
            else:
                ans.append(part)
                part=[]
                part.append(A[i])
        ans.append(part)
        return ans





print(Solution().smallestRangeI([10,12,6,4,9,11,13,6]))