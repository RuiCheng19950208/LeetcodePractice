class Solution(object):
    def reverseWords(self, s):
        ans=''
        word=[]
        w=[]
        for i in range(len(s)):

            w.append(s[i])
            if s[i] == ' ' :
                w.pop(-1)
                word.append(w[::-1])
                w=[]
            if i==len(s)-1:
                word.append(w[::-1])



        for i in range(len(word)):
            for j in range(len(word[i])):
                ans=ans+str(word[i][j])
            if i!=len(word)-1:
                ans=ans+' '


        return ans



print(Solution().reverseWords("Let's take LeetCode contest"))

