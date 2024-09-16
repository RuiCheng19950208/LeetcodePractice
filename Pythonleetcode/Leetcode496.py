class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        def nextbig(i,nums):
            mark=0
            for x in nums:
                if x==i:
                    mark=1
                if x>i and mark==1:
                    return x
            return -1


        ans=[]
        for i in findNums:
            ans.append(nextbig(i,nums))
        return ans



print(Solution().nextGreaterElement([4,1,2],  [1,3,4,2]))
print(Solution().nextGreaterElement([2,4], [1,2,3,4]))