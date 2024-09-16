class Solution(object):
    def isValid(self, s):

        dict={'(':')','[':']',"{":"}"}
        find_right=[]
        for i in range(len(s)):
            if s[i] in dict:
                find_right.append(dict[s[i]])
            elif len(find_right)==0 or s[i]!=find_right[-1]:
                return False
            elif  s[i]==find_right[-1]:
                find_right.pop()


        return len(find_right)==0




print(Solution().isValid('[]{}()'))
print(Solution().isValid('[(])'))


