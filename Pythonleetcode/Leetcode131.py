class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def dfs(s, temp):
            if s=='':
                self.res.append(temp[:])
                return
            for i in range(1,len(s)+1):
                if s[:i]==s[:i][::-1]:
                    # print(s,temp)
                    temp.append(s[:i])
                    dfs(s[i:],temp)
                    temp.pop()
            return
        self.res=[]
        dfs(s,[])
        return self.res





print(Solution().partition("aab"))