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
    vector<int> nums;
    vector<vector<int>> ans;
    int public_k = 0;
    void helper(vector<int>& nums, vector<int>& temp, int start) {
        if (temp.size() == public_k)
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
    vector<vector<int>> combine(int n, int k) {
        for (int i = 1; i <= n; i++)
        {
            nums.push_back(i);
        }
        int start = 0;
        public_k = k;
        vector<int> temp;
        helper(nums, temp, start);
        return ans;

    }
};