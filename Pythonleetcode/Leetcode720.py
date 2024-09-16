class Solution(object):
    def longestWord(self, words):
        words=sorted(words)
        res=set([''])
        longest=''
        for i in words:
            if i[:-1] in res:
                res.add(i)
                if  len(i)>len(longest):
                    longest=i
        return longest







print(Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))