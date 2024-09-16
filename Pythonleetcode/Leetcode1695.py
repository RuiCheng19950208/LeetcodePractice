class Solution(object):
    def maximumUniqueSubarray(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        fast=0
        slow=0
        ans=nums[0]
        temp_ans=nums[0]
        temp_list=[nums[0]]
        while fast<len(nums)-1:
            fast+=1
            while nums[fast] in temp_list:
                temp_list.pop(0)
                temp_ans-=nums[slow]
                slow += 1
            temp_list.append(nums[fast])
            temp_ans+=nums[fast]
            ans=max(ans,temp_ans)
            # print(slow, fast, ans)

        return ans

print(Solution().maximumUniqueSubarray(nums = [4,2,4,5,6]))
print(Solution().maximumUniqueSubarray(nums = [5,2,1,2,5,2,1,2,5]))
