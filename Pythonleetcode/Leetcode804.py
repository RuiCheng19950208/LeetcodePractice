class Solution(object):
    def uniqueMorseRepresentations(self, words):
        translation=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        result=[]
        for i in range(len(words)):
            s=''
            for j in range(len(words[i])):
                s=s+translation[alpha.index(words[i][j])]
            result.append(s)
        result=list(set(result))
        return len(result)



print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))