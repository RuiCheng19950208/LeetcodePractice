#include "LeetcodeHeader.h"

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n, vector<int>(n, 0));
        int row_begin = 0;
        int row_end = n - 1;
        int col_begin = 0;
        int col_end = n - 1;
        int myNum = 1;
        while (myNum <= n * n) {
            for (int i = col_begin; i <= col_end; i++)
            {
                ans[row_begin][i] = myNum;
                myNum++;

            }
            row_begin++;
            for (int i = row_begin; i <= row_end; i++)
            {
                ans[i][col_end] = myNum;
                myNum++;
            }
            col_end--;
            for (int i = col_end; i >=col_begin ;i--)
            {
                ans[row_end][i] = myNum;
                myNum++;
            }
            row_end--;
            for (int i = row_end; i >= row_begin ;i--)
            {
                ans[i][col_begin] = myNum;
                myNum++;
            }
            col_begin++;
        }

        return ans;
                    

    }
};