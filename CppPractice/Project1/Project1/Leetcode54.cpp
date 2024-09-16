#include "LeetcodeHeader.h"

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int col_begin = 0;
        int col_end = matrix[0].size() - 1;
        int row_begin = 0;
        int row_end = matrix.size() - 1;
        int myNum = 1;
        vector<int> ans;
        while (myNum <= matrix[0].size() * matrix.size())
        {
            for (int i = col_begin; i <= col_end; i++)
            {
                ans.push_back(matrix[row_begin][i]);
                myNum++;

            }
            row_begin++;
            if (row_begin>row_end)
            {
                break;

            }
            for (int i = row_begin; i <= row_end; i++)
            {

                ans.push_back(matrix[i][col_end]);
                myNum++;

            }
            col_end--;
            if (col_begin > col_end)
            {
                break;

            }
            for (int i = col_end; i >= col_begin; i--)
            {
                ans.push_back(matrix[row_end][i]);
                myNum++;


            }
            row_end--;
            for (int i = row_end; i >= row_begin; i--)
            {
                ans.push_back(matrix[i][col_begin]);
                myNum++;


            }
            col_begin++;
        }
        return  ans;

    }
};