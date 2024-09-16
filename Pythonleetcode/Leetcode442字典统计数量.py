class Solution(object):
    def findDuplicates(self, nums):
        dict1={}
        for i in range(len(nums)):
            dict1[nums[i]] = dict1.get(nums[i],0) + 1
        ans=[]
        for i in dict1:
            if dict1[i]>1:
                ans.append(i)
        return ans


print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))