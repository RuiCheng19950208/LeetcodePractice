class Solution(object):
    def maxNumberOfBalloons(self, text):
        ans_dict={}
        for i in text:
            if i not in ans_dict.keys():
                ans_dict[i]=1
            else:
                ans_dict[i]+=1
        if "b" not in ans_dict.keys() or "a"  not in ans_dict.keys() or "l"  not in ans_dict.keys() or "o"  not in ans_dict.keys() or "n"  not in ans_dict.keys():
            return 0
        ans=0
        while(ans_dict["b"]>=1 and ans_dict["a"]>=1 and ans_dict["l"]>=2 and ans_dict["o"]>=2 and ans_dict["n"]>=1 ):
            ans+=1
            ans_dict["b"]-=1
            ans_dict["a"] -= 1
            ans_dict["l"] -= 2
            ans_dict["o"] -= 2
            ans_dict["n"] -= 1
        return ans
print(Solution().maxNumberOfBalloons(text = "nlaebolko"))
print(Solution().maxNumberOfBalloons(text = "loonbalxballpoon"))
print(Solution().maxNumberOfBalloons(text = "leetcode"))