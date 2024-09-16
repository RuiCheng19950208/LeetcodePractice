class Solution(object):
    def jump(self, nums):
        if len(nums)==1:
            return 0
        max_reach=nums[0]
        previous_reach=0
        jump=0
        if max_reach >= len(nums) - 1:
            return 1
        while max_reach<len(nums)-1:
            low_index=previous_reach+1
            hi_index=max_reach+1
            for i in range(low_index,hi_index):
                max_reach=max(i+nums[i],max_reach)
            previous_reach=hi_index-1
            jump +=1
            if max_reach>=len(nums)-1:
                return jump+1

print(Solution().jump([2,3,1,1,4]))