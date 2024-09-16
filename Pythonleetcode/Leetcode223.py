class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):

        A1=(C-A)*(D-B)
        A2=(G-E)*(H-F)

        K1=max(min(C,G)-max(A,E),0)
        K2=max(min(D,H)-max(B,F),0)





        return A1+A2-max((K1*K2),0)





print(Solution().computeArea( -3, 0, 3, 4, 0, -1, 9, 2))