class Solution(object):
    def matrixReshape(self, nums, r, c):
        if r*c!=len(nums)*len(nums[0]):
            return nums
        else:
            ans=[]
            for i in nums:
                ans=ans+i
        res=[]
        ele=len(nums)*len(nums[0])


        for i in range(0,r):
            res.append(ans[int(i*(ele/r)):int((i+1)*(ele/r))])

        return res




print(Solution().matrixReshape([[1,2],[3,4]],1, 4))