class Solution(object):
    def reverseStr(self, s, k):
        n=1
        if 2*k*n>len(s):
            s=s[:k*n][::-1]+s[k*n:]
            return s
        while 2*k*n<=len(s):
            if 2*k*(n+1)>=len(s) and len(s) - 2*k*n<k:
                s = s[: 2 * k * (n - 1)] + s[2 * k * (n - 1):2 * k * (n - 1) + k][::-1] + s[2 * k * (n - 1) + k:]
                s=s[:2*k*n]+s[(2*k*n):][::-1]
              
            elif 2*k*(n+1)>=len(s) and len(s) - 2*k*n>=k:
                s = s[: 2 * k * (n - 1)] + s[2 * k * (n - 1):2 * k * (n - 1) + k][::-1] + s[2 * k * (n - 1) + k:]
                s=s[:2*k*n]+s[(2*k*n):(2*k*n)+k][::-1]+s[(2*k*n)+k:]

            else:
                s = s[: 2 * k * (n - 1)] + s[2 * k * (n - 1):2 * k * (n - 1) + k][::-1] + s[2 * k * (n - 1) + k:]



            n=n+1

        return s





print(Solution().reverseStr("abcdef",2))