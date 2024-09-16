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
    Solution(vector<int>& nums) {
        Solution::nums = nums;
        srand(time(NULL));
    }
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return nums;
    }
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        int ind;
        vector<int> ans = Solution::nums;
        int ans_size = ans.size();
        for (int i = 0; i < ans_size; i++)
        {
            ind = rand() % ans_size;
            swap(ans[i], ans[ind]);
        }
        return ans;

    }
};
