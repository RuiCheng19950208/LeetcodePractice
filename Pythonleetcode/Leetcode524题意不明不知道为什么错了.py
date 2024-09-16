class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        s_dict={}
        dictionary.sort()
        ans=""
        for i in s:
            s_dict.setdefault(i,0)
            s_dict[i]+=1
        keys=s_dict.keys()
        max_len=0
        for i in dictionary:
            temp_dict={}
            temp_len=0
            choose=True
            for s in i:
                if s not in keys:
                    choose=False
                    break
                temp_dict.setdefault(s, 0)
                temp_dict[s]+=1
                if s_dict[s]<temp_dict[s]:
                    choose = False
                    break
                temp_len+=1
            if choose and temp_len>max_len:
                ans=i
                max_len=temp_len

        return ans

print(Solution().findLongestWord( s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))
print(Solution().findLongestWord( s = "abpcplea", dictionary = ["a","b","c"]))
print(Solution().findLongestWord( s = "abpcplea", dictionary = ["ale","apple","monkey","plea", "abpcplaaa","abpcllllll","abccclllpppeeaaaa"]))

