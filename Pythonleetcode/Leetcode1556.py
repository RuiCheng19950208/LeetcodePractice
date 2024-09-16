class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """

        str_n=str(n)
        len_n=len(str_n)
        a=[]
        while len_n//3>0 and len_n>3:
            a.append(str_n[-3:])
            len_n -= 3
            str_n = str_n[:-3]
        a.append(str_n)
        a=a[::-1]

        ans=''
        for i in range(len(a)):
            if i!=len(a)-1:
                ans += a[i]+'.'
            else:
                ans += a[i]


        return ans

print(Solution().thousandSeparator(987))
print(Solution().thousandSeparator(9876))
print(Solution().thousandSeparator(98765432123456))

