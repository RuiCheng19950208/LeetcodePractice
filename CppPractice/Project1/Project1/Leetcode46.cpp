#include "LeetcodeHeader.h"

class Solution {
public:
    vector<vector<int>> ans;
    void helper(vector<int> &nums,vector<int> &temp) {
        if (nums.size()==temp.size())
        {
            ans.push_back(temp);
            return;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            if (find(temp.begin(),temp.end(),nums[i])==temp.end())
            {
                temp.push_back(nums[i]);
                helper(nums, temp);
                temp.pop_back();
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> temp;
        helper(nums,temp);
        return ans;

    }
};