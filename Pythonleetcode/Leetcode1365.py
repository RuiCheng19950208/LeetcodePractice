class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        nums_sort=sorted(nums)
        prev=nums_sort[0]
        num_cnt=0
        nums_dict = {prev: num_cnt}
        for i in range(1,len(nums_sort)):
            num_cnt += 1
            if nums_sort[i]!=prev:
                prev = nums_sort[i]
                nums_dict[prev]= num_cnt
        ans = []
        for i in range(len(nums)):
            ans.append(nums_dict[nums[i]])
        return ans





print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))
print(Solution().smallerNumbersThanCurrent([6,5,4,8]))
print(Solution().smallerNumbersThanCurrent([7,7,7,7]))

