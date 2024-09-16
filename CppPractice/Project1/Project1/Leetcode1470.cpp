#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

using namespace std;


class Solution1470 {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> ans;
        for (int i = 0; i < n;i++) {
            ans.push_back(nums[i]);
            ans.push_back(nums[i+n]);
        }
        return ans;


    }
};