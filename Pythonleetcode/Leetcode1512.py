class Solution(object):
    def numIdenticalPairs(self, nums):
        def conbinition_num(y):
            if y<2:
                return 0
            else:
                return int(y*(y-1)/2)

        nums=sorted(nums)
        ans=0
        for i in set(nums):
            ans += conbinition_num(nums.count(i))

        return ans



print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
print(Solution().numIdenticalPairs([1,1,1,1]))
print(Solution().numIdenticalPairs([1,2,3]))