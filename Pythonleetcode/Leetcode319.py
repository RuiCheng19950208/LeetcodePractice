# class Solution(object):
#     def bulbSwitch(self, n):
#         def change(light,i):
#             for x in range(i,len(light)):
#                 if (x+1)%(i+1)==0 and light[x]==0:
#                     light[x]=1
#                 elif (x+1)%(i+1)==0 and light[x]==1:
#                     light[x]=0
#
#             return light
#
#         if n==1:
#             return 1
#         light=[0]*n
#         for i in range(n):
#             light=change(light,i)
#         return light.count(1)
# 爆破失败

# https://blog.csdn.net/baidu_23318869/article/details/50386323 妙法破解


class Solution(object):
    def bulbSwitch(self, n):
        return int(n**0.5)





print(Solution().bulbSwitch(3))
print(Solution().bulbSwitch(5))
print(Solution().bulbSwitch(8))