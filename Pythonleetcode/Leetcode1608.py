class Solution(object):
    def specialArray(self, nums):
        nums.sort()
        ans_dict={}
        for i in range(len(nums)):
            if nums[i] not in ans_dict.keys():
                ans_dict[nums[i]]=len(nums)-i
        print(ans_dict)
        thresh=0
        for i in sorted(list(ans_dict.keys())):
            if i>=ans_dict[i] and ans_dict[i]>thresh:
                return ans_dict[i]
            else:
                thresh=i
        return -1

# print(Solution().specialArray(nums = [3,5]))
# print(Solution().specialArray(nums = [0,0]))
# print(Solution().specialArray(nums = [3,6,7,7,0]))
print(Solution().specialArray(nums=[3,9,7,8,3,8,6,6]))



