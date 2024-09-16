class Solution(object):
    def validPalindrome(self, s):
        print(s[:0])
        for i in range(0, len(s)):
            if s[i] != s[len(s) - 1 - i]:

                if self.check(s[:i] + s[i + 1:]) == False and self.check(s[:len(s) - 1 - i] + s[len(s) - i:]) == False:
                    return False

                else:
                    return True

        return True
    def check(self, s):
        for i in range(0, len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True



print(Solution().validPalindrome("labcba"))