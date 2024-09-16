class Solution(object):
    def longestCommonPrefix(self, strs):
        res=''
        m=0
        min=100
        if len(strs)==1:
            return strs[0]
        for i in range(0,len(strs)):
            if len(strs[i])<min:
                min=len(strs[i])

        for j in range(0, min):
            for i in range(1,len(strs)):

                if strs[i][j]==strs[i-1][j]:
                    m=m+1
                    if m==len(strs)-1:
                        res=res+strs[i][j]
                        print(m)
                else:
                    return res
            m = 0


        return res

print(Solution().longestCommonPrefix(["flower","flow","fliwht"]))