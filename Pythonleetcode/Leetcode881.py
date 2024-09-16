class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        ans=0
        while len(people)>0:
            l=0
            r=len(people)-1
            if people[r]+people[l]>limit:
                ans+=1
                people.pop()
            else:
                ans+=1
                if l!=r:
                    people.pop(0)
                people.pop()
        return ans

print(Solution().numRescueBoats(people = [1,2], limit = 3))
print(Solution().numRescueBoats(people = [3,2,2,1], limit = 3))
print(Solution().numRescueBoats(people = [3,5,3,4], limit = 5))