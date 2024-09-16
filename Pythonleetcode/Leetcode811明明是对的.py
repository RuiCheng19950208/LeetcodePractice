class Solution(object):
    def subdomainVisits(self, cpdomains):
        num=[]
        string=[]
        for i in range(len(cpdomains)):
            for j in range(len(cpdomains[i])):
                if cpdomains[i][j]== " ":
                    num.append(int(cpdomains[i][:j]))
                    string.append(cpdomains[i][j+1:])
                    continue

        for i in range(len(string)):
            for j in range(len(string[i])):
                if string[i][j]==".":
                    if string[i][j+1:] not in string:
                        string.append(string[i][j+1:])
                        num.append(num[i])
                    else:
                        num[string.index(string[i][j+1:])]=num[string.index(string[i][j+1:])]+num[i]

        result=[]
        for i in range(len(num)):
            result.append(str(num[i])+" "+ string[i])





        return result






print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))