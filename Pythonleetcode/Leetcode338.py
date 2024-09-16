class Solution(object):
    def countBits(self, num):
        ans=[]
        for i in range(num+1):
            ans.append(bin(i).count('1'))
        return ans



print(Solution().countBits(5))