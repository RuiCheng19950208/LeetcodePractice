class Solution(object):
    def compress(self, chars):
        setc=list(set(chars))
        coun=[]
        extra=0
        for i in setc:
            a=chars.count(i)
            if a>100:
                coun.append(a)
                extra=extra+2
            elif a > 10:
                coun.append(a)
                extra = extra + 1
            elif a > 1:
                coun.append(a)



        return len(setc)+len(coun)+extra







print(Solution().compress(["a","a","b","b","c","c","c"]))
print(Solution().compress(["a"]))
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))