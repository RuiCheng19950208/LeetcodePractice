class Solution(object):
    def subarraySum(self, nums, k):
        prefix_dict={}
        ans=0
        for i in range(len(nums)):
            a=sum(nums[:i+1])
            if  a-k in prefix_dict:
                ans += prefix_dict[a - k]
            prefix_dict[a]=prefix_dict.setdefault(a,0)+1
            if a-k==0:
                ans+=1
            # print(prefix_dict,ans)
        return ans

print(Solution().subarraySum(nums = [1,1,1], k = 2))
print(Solution().subarraySum(nums = [1,2,3], k = 3))
print(Solution().subarraySum(nums = [1], k = 0))