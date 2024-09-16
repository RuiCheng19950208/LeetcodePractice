#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

using namespace std;


class Solution1480 {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> ans;
        int temp_sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            temp_sum = temp_sum + nums[i];
            ans.push_back(temp_sum);
        }
        return ans;


    }
};