class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        vector_list=[]
        vector_length=[]
        max_length_index = 0
        vector_list.append([p4[0] - p1[0], p4[1] - p1[1]])
        vector_list.append([p3[0] - p1[0], p3[1] - p1[1]])
        vector_list.append([p2[0] - p1[0], p2[1] - p1[1]])
        for i in vector_list:
            vector_length.append((i[0]**2+i[1]**2)**0.5)
        for i in range(len(vector_length)):
            if vector_length[i]==max(vector_length):
                max_length_index=i
            if vector_length[i]==0:
                return False


        vector_short=[]
        vector_long =0
        for i in range(len(vector_length)):
            if i==max_length_index:
                vector_long=vector_list[i]
            else:
                vector_short.append(vector_list[i])


        def sum_short_length_equal_long_length_sqare(vector_short,vector_long):
            if(vector_short[0][0]**2+vector_short[0][1]**2+vector_short[1][0]**2+vector_short[1][1]**2==vector_long[0]**2+vector_long[1]**2):
                return True
            else:
                return False
        def two_vector_45_degree(vector_short,vector_long):
            vector_short_1_length = (vector_short[0][0] ** 2 + vector_short[0][1] ** 2) ** 0.5
            vector_short_2_length =(vector_short[1][0] ** 2 + vector_short[1][1] ** 2) ** 0.5
            vector_long_length =(vector_long[0] ** 2 + vector_long[1] ** 2) ** 0.5


            if (vector_long_length*vector_short_1_length)*(2**0.5/2) -(vector_short[0][0] * vector_long[0] + vector_short[0][1] * vector_long[1])<0.01and (vector_long_length*vector_short_2_length)*(2**0.5/2) - (vector_short[1][0] * vector_long[0] + vector_short[1][1] * vector_long[1])<0.01:
                return True
            else:
                return False

        def two_short_vertical(vector_short):


            if (vector_short[0][0]*vector_short[1][0]+vector_short[0][1]*vector_short[1][1])==0:
                return True
            else:
                return False

        def check_square(vector_short,vector_long):
            # print(sum_short_length_equal_long_length_sqare(vector_short,vector_long),two_vector_45_degree(vector_short,vector_long) ,two_short_vertical(vector_short))
            if(sum_short_length_equal_long_length_sqare(vector_short,vector_long) and two_vector_45_degree(vector_short,vector_long) and two_short_vertical(vector_short)):
                return True
            else:
                return False

        if check_square(vector_short,vector_long):
            return True
        else:
            return False



print(Solution().validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))
print(Solution().validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]))
print(Solution().validSquare(p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]))