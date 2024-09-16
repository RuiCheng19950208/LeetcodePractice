#include "LeetcodeHeader.h"

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        vector<int> temp;
        if (numRows == 0)
        {
            return ans;
        }
        else if (numRows == 1)
        {
            temp = { 1 };
            ans.push_back(temp);
            return ans;
        }
        else if (numRows == 2)
        {
            temp = { 1 };
            ans.push_back(temp);
            temp = { 1,1 };
            ans.push_back(temp);
            return ans;

        }
        else
        {
            temp = { 1 };
            ans.push_back(temp);
            temp = { 1,1 };
            ans.push_back(temp);
            for (int i = 3; i <= numRows; i++)
            {
                temp = { };
                for (int j = 0; j < i; j++)
                {
                    if (j == 0 or j == i - 1)
                    {
                        temp.push_back(1);
                    }
                    else
                    {
                        temp.push_back(ans.back()[j - 1] + ans.back()[j]);
                    }
                }
                ans.push_back(temp);
            }

        }

        return ans;
    }
};