class Solution:
    def nthUglyNumber(self, n):
        if n <= 0:
            return False
        t1=0
        t2=0
        t3=0
        ans=[1]
        a=1
        while a!=n:
            a=a+1
            ans.append(min([ans[t1]*2,ans[t2]*3,ans[t3]*5]))
            print(ans)
            if ans[t1]*2==ans[-1]:
                t1=t1+1
            if ans[t2]*3==ans[-1]:
                t2=t2+1
            if ans[t3]*5==ans[-1]:
                t3=t3+1
        return ans[-1]


print(Solution().nthUglyNumber(10))
