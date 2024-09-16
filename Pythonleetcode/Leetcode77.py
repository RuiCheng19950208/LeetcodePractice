# class Solution(object):
#     def combine(self, n, k):
#         res=[]
#         sub = []
#
#         def back(SUB):
#             for i in range(1, n + 2):
#                 if i in SUB or (SUB!=[] and i<=max(SUB)):
#                     continue
#                 if len(SUB)==k:
#                     if SUB not in res:
#                         res.append(SUB)
#                 x=SUB[:]
#                 x.append(i)
#                 back(x)
#
#
#
#         back(sub)
#
#         return res


class Solution(object):
    def combine(self, n, k):
        def back(res, i, n, k, sub):
            if k == 0:
                res.append(sub)
            for j in range(i + 1, n + 1):
                back(res, j, n, k - 1, sub + [j])


        res = []
        back(res, 0, n, k, [])
        return res




print(Solution().combine(4,2))