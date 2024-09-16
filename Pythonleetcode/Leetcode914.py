class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck)<=1:
            return False
        set_deck=list(set(deck))
        count_set=[deck.count(i) for i in set_deck]
        for i in range(2,len(deck)+1):
            if all(j%i==0 for j in count_set):
                return True
        return False


print(Solution().hasGroupsSizeX(deck = [1,2,3,4,4,3,2,1]))
print(Solution().hasGroupsSizeX(deck = [1,1,1,2,2,2,3,3]))
print(Solution().hasGroupsSizeX(deck = [1]))
print(Solution().hasGroupsSizeX(deck = [1,1,2,2,2,2]))

