class Solution(object):
    def decrypt(self, code, k):
        ans=[0]*len(code)
        ans_list=code*1
        if k==0:
            return ans
        if k<0:
            ans_list=ans_list[::-1]
        for i in range(len(code)):
            if k>0:
                ans_list=ans_list[1:]+ans_list[:1]
                ans[i]=sum(ans_list[:k])
            else:
                ans[i] = sum(ans_list[:-k])
                ans_list = ans_list[-1:] + ans_list[:-1]
        return ans

print(Solution().decrypt( code = [5,7,1,4], k = 3))
print(Solution().decrypt( code = [1,2,3,4], k = 0))
print(Solution().decrypt( code = [2,4,9,3], k = -2))
print(Solution().decrypt( code = [5,2,2,3,1],k = 3))
print(Solution().decrypt( code = [10,5,7,7,3,2,10,3,6,9,1,6],k = -4))
