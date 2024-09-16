class Solution(object):
    def restoreString(self, s, indices):
        ans=['A']*len(indices)
        for i in range(len(indices)):
            ans[indices[i]]=s[i]

        print(ans)

        result=''
        for i in ans:
            result+=i

        return result
print(Solution().restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))