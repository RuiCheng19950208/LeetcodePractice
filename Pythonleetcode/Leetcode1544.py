class Solution(object):
    def makeGood(self, s):
        if len(s)<=1:
            return s
        temp_index=0
        len_s=len(s)
        while temp_index<=len_s-2:
            if (s[temp_index].lower()==s[temp_index+1] and s[temp_index].isupper()) or (s[temp_index].upper()==s[temp_index+1] and s[temp_index].islower()):
                s=s[:temp_index]+s[temp_index+2:]
                len_s-=2
                if temp_index>=1:
                    temp_index-=1
                else:
                    temp_index =0
            else:
                temp_index+=1
        return s

print(Solution().makeGood(s = "leEeetcode"))
print(Solution().makeGood(s = "abBAcC"))
print(Solution().makeGood(s = "s"))