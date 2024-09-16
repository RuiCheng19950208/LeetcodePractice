class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        string1=""
        string2=""
        for i in word1:
            string1+=i
        for i in word2:
            string2 += i
        return string1==string2

print(Solution().arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
print(Solution().arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]))
print(Solution().arrayStringsAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]))