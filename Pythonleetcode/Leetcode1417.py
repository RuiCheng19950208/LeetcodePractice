class Solution(object):
    def reformat(self, s):
        num_list=['0','1','2','3','4','5','6','7','8','9']
        num_str=""
        word_str=""
        for i in s:
             if i in num_list:
                 num_str+=i
             else:
                 word_str+=i
        ans=""
        if abs(len(num_str)-len(word_str))>=2:
            return ""
        if len(num_str)-len(word_str)>=0:
            for i in range(len(word_str)):
                ans+=num_str[i]
                ans+=word_str[i]
            if len(num_str)-len(word_str)==0:
                return ans
            else:
                return ans+num_str[-1]
        if len(num_str) - len(word_str) == -1:
            for i in range(len(num_str)):
                ans+=word_str[i]
                ans += num_str[i]
            return ans+word_str[-1]

print(Solution().reformat( s = "a0b1c2"))
print(Solution().reformat( s = "leetcode"))
print(Solution().reformat( s = "1229857369"))
print(Solution().reformat( s = "covid2019"))
print(Solution().reformat( s = "ab123"))