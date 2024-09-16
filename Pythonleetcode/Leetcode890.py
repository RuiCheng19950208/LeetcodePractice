class Solution(object):
    def findAndReplacePattern(self, words, pattern):

        def ispat(w,p):
            if len(set(w))==len(set(p))==len(set(zip(w,p))):

                return True
            else: return False

        ans=[]

        for i in words:

            if ispat(i,pattern):
                ans.append(i)
        return ans




print(Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))