class Solution(object):
    def fairCandySwap(self, A, B):

        he1 = sum(A)
        he2 = sum(B)
        cha = (he1 - he2) / 2
        setB = set(B)

        for i in A:
            if i - cha in setB:
                return [i, i - cha]







print(Solution().fairCandySwap([1,1],  [2,2]))
print(Solution().fairCandySwap([1,2],  [2,3]))
print(Solution().fairCandySwap([2],    [1,3]))
print(Solution().fairCandySwap([1,2,5], [2,4]))