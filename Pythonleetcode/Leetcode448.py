class Solution(object):
    def findDisappearedNumbers(self, nums):
        if nums==[]:
            return []
        a=[]
        for i in range(1,len(nums)+1):
            a.append(i)
        nums=sorted(list(set(nums)))
        ans=list(set(a).difference(set(nums)))
        return ans




print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))