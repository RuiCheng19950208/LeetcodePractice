# Approach 1
# class Solution(object):
#     def letterCombinations(self,digits):
#         nums=['','',"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
#         out=[]
#         for i in range(len(digits)):
#             x=int(digits[i])
#
#             for j in range(len(nums[x])):
#                 if i==0:
#                     out.append(nums[x][j])
#                 else:
#                     for m in range(len(out)):
#                         if len(out[m])==i:
#                             out.append(out[m]+nums[x][j])
#
#         ans=[]
#         for i in out:
#             if len(i)==len(digits):
#                 ans.append(i)
#
#
#         return ans


# Approach 2

class Solution(object):
    def letterCombinations(self,digits):
        self.dict={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        self.out=[]
        if not digits:
            return []
        def dfs(string,index,temp):

            if len(temp)==len(digits):
                self.out.append(''.join(x for x in temp))
                return
            for char in self.dict[string[index]]:
                temp.append(char)
                dfs(string,index+1,temp)
                temp.pop()
            return
        dfs(digits,0,[])
        return self.out


print(Solution().letterCombinations("23"))
print(Solution().letterCombinations("5"))