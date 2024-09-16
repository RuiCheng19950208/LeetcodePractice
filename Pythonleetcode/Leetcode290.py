class Solution(object):
    def wordPattern(self, pattern, str):
        str=str.split()
        if len(str)!=len(pattern):
            return False

        n=0
        pair=[]
        capital=[]
        lat=[]
        while(n<len(str)):
            if pattern[n] not in capital:
                capital.append(pattern[n])

                pair.append(pattern[n]+str[n])
                if str[n] in lat:
                    return False
                lat.append(str[n])
            elif pattern[n]+str[n] not in pair:
                return False
            n=n+1

        return True


print(Solution().wordPattern( "abba", "dog cat cat dog"))
print(Solution().wordPattern( "aaaa", "dog dog dog dog"))
print(Solution().wordPattern( "abba","dog dog dog dog" ))