class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted(nums)
        ans=sum(nums)

        yu1=sorted([i for i in nums if i%3==1])
        yu2=sorted([i for i in nums if i%3==2])

        if ans%3==0:
            return ans
        elif ans%3==1:
            if len(yu2)>1 and len(yu1)>0:
                return ans-min(yu1[0],yu2[0]+yu2[1])
            elif len(yu1)>0:
                return ans -yu1[0]
            elif len(yu2)>1:
                return ans -yu2[0]-yu2[1]
            else: return 0

        else:
            if len(yu2)>0 and len(yu1)>1:
                return ans-min(yu1[0]+yu1[1],yu2[0])
            elif len(yu2)>0:
                return ans -yu2[0]
            elif len(yu1)>1:
                return ans -yu1[0]-yu1[1]
            else:
                return 0





print(Solution().maxSumDivThree([3,6,5,1,8]))
print(Solution().maxSumDivThree([4]))
print(Solution().maxSumDivThree([1,2,3,4,4]))
print(Solution().maxSumDivThree([5,2,2,2]))