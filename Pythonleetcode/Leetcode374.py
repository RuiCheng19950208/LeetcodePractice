class Solution(object):
    def guessNumber(self, n):
        start = 1
        end = n
        ans = int((1 + n) / 2)
        print(ans)
        while start != end:
            if guess(ans) == 1:
                start = ans + 0
                ans = int((start + end) / 2) + 1
                print([start, end], ans)
                continue

            if guess(ans) == -1:
                end = ans + 0
                ans = int((start + end) / 2)
                print('wow')

                continue

            if guess(ans) == 0:
                return ans
        return ans



