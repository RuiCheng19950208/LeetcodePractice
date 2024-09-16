#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

#include <bitset>

using namespace std;


class Solution {
public:
    vector<vector<int>> ans;
    void helper(vector<int>& nums, vector<int>& temp,int start)
    {

        if (find(ans.begin(), ans.end(), temp) == ans.end())
        {
            ans.push_back(temp);
          
        }
        for (int i = start; i < nums.size(); i++)
        {
            temp.push_back(nums[i]);
            helper(nums, temp, i + 1);
            temp.pop_back();
        }
        return;

    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> temp;
        int start = 0;
        helper(nums, temp,start);
        return ans;

    }
};