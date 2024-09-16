class Solution(object):
    def findShortestSubArray(self, nums):
        dict_nums={}
        for i in range(len(nums)):
            if nums[i] not in dict_nums:
                dict_nums[nums[i]]=[1,i,i]
            else:
                dict_nums[nums[i]][0] += 1
                dict_nums[nums[i]][2] =i
        degree=0
        for i in dict_nums:
            if dict_nums[i][0]>degree:
                degree=dict_nums[i][0]
        min_len=10**10
        for i in dict_nums:
            if dict_nums[i][0]==degree and dict_nums[i][2]-dict_nums[i][1]+1<min_len:
                min_len=dict_nums[i][2]-dict_nums[i][1]+1

        return min_len





print(Solution().findShortestSubArray( [1,2,2,3,1]))
print(Solution().findShortestSubArray( [1,2,2,3,1,4,2]))
