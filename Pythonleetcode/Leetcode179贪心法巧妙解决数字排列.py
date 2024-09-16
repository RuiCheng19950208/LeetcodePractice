class Solution(object):
    def largestNumber(self, nums):
        def big(a,b):
            if int(str(a)+str(b))<int(str(b)+str(a)):
                return True
            else: return False

        for i in range(0,len(nums)-1):
            for j in range(i,len(nums)):
                if big(nums[i],nums[j])==True:
                    nums[i], nums[j]=nums[j],nums[i]

        ans=''
        for i  in nums:
            ans=ans+str(i)
        if ans[0]=='0' and len(ans)>1: #针对nums全零情形
            return '0'
        return ans




print(Solution().largestNumber([3,30,34,5,9]))