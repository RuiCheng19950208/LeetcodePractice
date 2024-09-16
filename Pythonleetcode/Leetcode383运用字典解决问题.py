class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(magazine)<len(ransomNote):
            return False
        dict1={}
        dict2={}
        for i in range(len(ransomNote)):
            dict1[ransomNote[i]] = dict1.get(ransomNote[i],0) + 1
        for i in range(len(magazine)):
            dict2[magazine[i]] = dict2.get(magazine[i],0) + 1
        for i in dict1.keys():
            if i not in dict2.keys() or dict1[i]>dict2[i]:
                return False
        return True





print(Solution().canConstruct("aa", "aab"))
print(Solution().canConstruct("a", "b"))
print(Solution().canConstruct("aa", "ab"))