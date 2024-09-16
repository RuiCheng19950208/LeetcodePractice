# class Solution(object):
#     def findRepeatedDnaSequences(self, s):
#         ans=[]
#         for i in range(len(s)-9):
#             key=s[i:i+10]
#             if key in s[i+1:] and key not in ans :
#                 ans.append(key)
#         return list(set(ans))
# 13800ms勉强通过


class Solution(object):
    def findRepeatedDnaSequences(self, s):

                seen = set()
                repeated = set()
                N = len(s)
                for i in range(N):
                    cur = s[i: i + 10]
                    if cur in seen:
                        repeated.add(cur)
                    else:
                        seen.add(cur)
                return list(repeated)
#一个巧妙的避免在过长的字符串中搜索的算法

print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))