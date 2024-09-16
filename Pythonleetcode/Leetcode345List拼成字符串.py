class Solution(object):
    def reverseVowels(self, s):
        vowel=[]
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:

                vowel.append(s[i])
        vowel=vowel[::-1]
        s=list(s)#关键

        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                s[i]=vowel[0]
                vowel.pop(0)
        return ''.join(s) #关键

#慎用append，容易超时






print(Solution().reverseVowels("leetcode"))