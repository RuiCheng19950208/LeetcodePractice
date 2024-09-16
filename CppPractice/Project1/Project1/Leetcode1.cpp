#include "LeetcodeHeader.h"

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans(2, 0);
        for (int i = 0; i < nums.size() - 1; i++)
        {
            ans = { i,0 };
            for (int j = i + 1; j < nums.size(); j++)
            {
                if (nums[j] == target - nums[i])
                {
                    ans[1] = j;
                    return ans;
                }
            }

        }


        return ans;
    }
};