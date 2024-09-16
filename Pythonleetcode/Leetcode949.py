class Solution(object):
    def largestTimeFromDigits(self, A):
        A=sorted(A)
        ans=''
        find2=0
        find1=0
        find0=0

        for i in A:
            if i==2:
                ans=ans+'2'
                A.pop(A.index(i))
                find2=1
                break


        if find2==0:
            for i in A:
                if i == 1:
                    ans = ans + '1'
                    A.pop(A.index(i))
                    find1 = 1
                    break


            if find1 == 0:
                for i in A:
                    if i == 0:
                        ans = ans + '0'
                        A.pop(A.index(i))
                        find0 = 1
                        break

                if find0==0:
                    return ''
                elif A[-2]<=5:
                    ans = ans + str(A[-1]) + ':' + str(A[-2]) + str(A[-3])
                    return ans

                elif A[-3] <= 5:
                    ans = ans + str(A[-1]) + ':' + str(A[-3]) + str(A[-2])
                    return ans

                else:
                    return ''




            elif A[-2]<=5:
                ans=ans+str(A[-1])+':'+str(A[-2])+str(A[-3])
                return ans
            elif A[-3]<=5:
                ans = ans + str(A[-1]) + ':' + str(A[-3]) + str(A[-2])
                return ans
            else:
                return ''





        elif A[0]<2 and A[-2]>5:
            return str(A[0])+str(A[-1])+':'+'2'+str(A[-2])


        elif A[-1]<=3:
            ans=ans+str(A[-1])+':'+str(A[-2])+str(A[-3])
            return ans
        elif A[-2]<=3:
            ans = ans + str(A[-2]) + ':'
            if A[-1]<=5:
                ans=ans+str(A[-1])+str(A[-3])
                return ans
            else:
                ans = ans + str(A[-3]) + str(A[-1])
                return ans

        elif A[-3] <= 3:
            ans = ans + str(A[-3]) + ':'
            if A[-1]<=5:
                ans=ans+str(A[-1])+str(A[-2])
                return ans
            elif A[-2]<=5:
                ans = ans + str(A[-2]) + str(A[-1])
                return ans
            else:
                return ''







        return ''









print(Solution().largestTimeFromDigits([1,2,3,4]))
print(Solution().largestTimeFromDigits([0,0,0,0]))
print(Solution().largestTimeFromDigits([6,6,2,0]))