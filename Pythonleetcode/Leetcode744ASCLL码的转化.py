class Solution(object):
    def nextGreatestLetter(self, letters, target):
        target=ord(target)
        letters=sorted(list(set(letters)))

        for i in range(len(letters)):
            if ord(letters[i])>target:
                return letters[i]
        return letters[0]



print(Solution().nextGreatestLetter( ["c", "f", "j"],'a'))