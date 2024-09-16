class Solution(object):
    def isPalindrome(self, s):
        k=''
        for i in range(0,len(s)):
            if s[i].isdigit() or s[i].isalpha():
                k=k+s[i]
        k=k.upper()
        for i in range(0,len(k)):
            if k[i]!=k[len(k)-1-i]:
                return False
        return True



print(Solution().isPalindrome("A man, a plan, a canal: Panama"))