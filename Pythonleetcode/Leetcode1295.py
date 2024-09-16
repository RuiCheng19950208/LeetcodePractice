class Solution(object):
    def findNumbers(self, nums):
        ans=0
        for i in nums:
            dig=0
            while True:
                if i//10!=0:
                    dig +=1
                    i=i//10
                else:
                    dig += 1
                    break
            if dig%2==0:
                ans +=1
        return ans






print(Solution().findNumbers( [12,345,2,6,7896]))
print(Solution().findNumbers( [555,901,482,1771]))



