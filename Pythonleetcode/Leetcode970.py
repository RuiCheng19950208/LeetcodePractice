class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        ans=[]
        for i in range(101):
            for j in range(101):
                res=x ** i + y ** j
                if res<=bound:
                    ans.append(res)
                else:continue

        return list(set(ans))











print(Solution().powerfulIntegers(2, 3, 10))
print(Solution().powerfulIntegers(3, 5, 15))