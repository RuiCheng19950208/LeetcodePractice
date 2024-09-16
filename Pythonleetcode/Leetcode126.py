class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        def is_just_one_char_diff(temp,word):
            diff=0
            for i in temp[-1]:
                if(temp[-1][i]!=word[i]):
                    diff+=1
            if diff==1:
                return True
            else:
                return False

        dp=[]
        temp=[]
        temp_word_list=[]

        return

print(Solution().findLadders(beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]))


print(Solution().findLadders(beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log"]))