class Solution(object):
    def defangIPaddr(self, address):
        ans=""
        for i in range(len(address)):
            if address[i] =='.':
                ans += '[.]'
            else:
                ans=ans + address[i]
        return ans






print(Solution().defangIPaddr("1.1.1.1"))
