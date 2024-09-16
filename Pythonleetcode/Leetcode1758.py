class Solution(object):
    def minOperations(self, s):
        dif1=0
        dif2=0
        t1,t2="",""
        for i in range(len(s)):
            if i%2==0:
                t1+='1'
                t2+="0"
            else:
                t1 += '0'
                t2 += "1"
        for i in range(len(s)):
            if s[i]!=t1[i]:
                dif1+=1
            if s[i]!=t2[i]:
                dif2+=1

        return min(dif1,dif2)

print(Solution().minOperations( s = "0100"))
print(Solution().minOperations(  s = "10"))
print(Solution().minOperations(  s = "1111"))