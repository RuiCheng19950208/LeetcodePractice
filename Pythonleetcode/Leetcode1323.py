class Solution(object):
    def maximum69Number (self, num):
        str_num=str(num)
        for i in range(len(str_num)):
            if str_num[i]=='6':
                str_num=str_num[:i]+'9'+str_num[i+1:]
                ans=int(str_num)
                return ans

        return num

print(Solution().maximum69Number(9669))
print(Solution().maximum69Number(9966))
print(Solution().maximum69Number(9999))
print(Solution().maximum69Number(9996))