class Solution(object):
    def constructRectangle(self, area):
        p=int(area**0.5)

        while area%p!=0:
            p=p-1

        return [area//p,p]






print(Solution().constructRectangle(10000000))