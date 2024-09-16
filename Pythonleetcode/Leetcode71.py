class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list=path.split('/')
        path_list=[i for i in path_list if len(i)>0]
        temp=[]
        # print(path_list)
        ans=''
        for i in path_list:
            if i=="." or (i==".." and len(temp)==0):
                continue
            elif i=="..":
                temp.pop()
            else:
                temp.append(i)
        if len(temp)>0:
            for i in temp:
                ans+='/'
                ans+=i
            return ans
        else:
            return "/"


print(Solution().simplifyPath(path = "/home/"))
print(Solution().simplifyPath(path = "/../"))
print(Solution().simplifyPath(path = "/a/./b/../../c/"))
print(Solution().simplifyPath(path = "/home//foo/"))
