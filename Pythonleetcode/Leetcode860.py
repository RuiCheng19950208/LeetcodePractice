class Solution(object):
    def lemonadeChange(self, bills):
        five=0
        ten=0
        for i in bills:
            if i==5:
                five=five+1
            elif i==10:
                ten=ten+1
                five=five-1
                if five<0:
                    return False
            elif i==20:

                if ten==0:
                    five=five-3
                else:
                    ten=ten-1
                    five=five-1
                if ten<0 or five<0:
                    return False
        return True


print(Solution().lemonadeChange([5,5,10]))