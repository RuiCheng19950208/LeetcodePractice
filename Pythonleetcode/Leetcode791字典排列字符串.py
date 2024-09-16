class Solution(object):
    def customSortString(self, S, T):
        dict1={}
        for i in range(len(T)):
            dict1[T[i]]= dict1.get(T[i],0) + 1

        ans=''
        for i in  S:
            ans=ans+i*dict1.get(i,0)
            dict1[i]=0
        for i in dict1:
            ans=ans+i*dict1.get(i,0)

        return ans









print(Solution().customSortString("cba","abcd"))
