
class Solution(object):
    def detectCapitalUse(self, word):
        Alpha={'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'}

        if set(word).intersection(set(Alpha))==set(word):
            return True
        if set(word.upper()).intersection(set(word))==set():
            return True
        if set(word[0]).intersection(set(Alpha))==set(word[0]) and set(word[1:]).intersection(set(Alpha))==set():
            return True
        return False



print(Solution().detectCapitalUse('USA'))
print(Solution().detectCapitalUse('usa'))
print(Solution().detectCapitalUse('Usa'))
print(Solution().detectCapitalUse('uSa'))