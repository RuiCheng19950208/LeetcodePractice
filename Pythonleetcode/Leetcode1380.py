class Solution(object):
    def luckyNumbers (self, matrix):
        col_all=[]
        for j in range(len(matrix[0])):
            temp_col=[]
            for i in range(len(matrix)):
                temp_col.append(matrix[i][j])
            col_all.append(temp_col)

        # print(col_all)
        ans=[]
        min_in_row_index=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if min(matrix[i])==matrix[i][j]:
                    min_in_row_index.append([i,j])

        for k in min_in_row_index:
            if col_all[k[1]][k[0]]==max(col_all[k[1]]):
                ans.append(col_all[k[1]][k[0]])
        return ans

print(Solution().luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]]))
print(Solution().luckyNumbers(matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(Solution().luckyNumbers(matrix = [[7,8],[1,2]]))