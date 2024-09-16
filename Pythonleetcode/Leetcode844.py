class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def deal_string(t):
            str_list=[]
            for i in t:
                if i=="#" and len(str_list):
                    str_list.pop()
                elif i!="#":
                    str_list.append(i)
            return "".join(str_list)
        return deal_string(S)==deal_string(T)

print(Solution().backspaceCompare( S = "ab#c", T = "ad#c"))
print(Solution().backspaceCompare( S = "ab##", T = "c#d#"))
print(Solution().backspaceCompare(  S = "a##c", T = "#a#c"))
print(Solution().backspaceCompare(  S = "a#c", T = "b"))

