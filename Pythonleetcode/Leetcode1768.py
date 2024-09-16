class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans=""
        record=min(len(word1),len(word2))
        for i in range(record):
            ans+=word1[i]+word2[i]

        if len(word1)>len(word2):
            ans+=word1[record:]

        if len(word1) < len(word2):
            ans += word2[record:]



        return ans

print(Solution().mergeAlternately(word1 = "abc", word2 = "pqr"))
print(Solution().mergeAlternately(word1 = "ab", word2 = "pqrs"))
print(Solution().mergeAlternately(word1 = "abcd", word2 = "pq"))