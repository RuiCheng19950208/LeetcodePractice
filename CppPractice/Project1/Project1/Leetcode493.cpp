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
    int reversePairs(vector<int>& nums) {

        return helper(0, nums.size() - 1, nums);

    }

    int helper(int begin, int end, vector<int>& nums) {
        int ans = 0;
        int mid = 0;
        if (begin >= end)
        {
            return 0;
        }
        else
        {
            mid = (begin + end) / 2;
            ans = helper(begin, mid, nums) + helper(mid + 1, end, nums);
            sort(nums.begin(), nums.begin() + mid + 1);
            sort(nums.begin() + mid, nums.end());

            int idx_1 = begin;
            int idx_2 = mid + 1;

            while (idx_1 <= mid and idx_2 <= end)
            {
                if ((long)nums[idx_1] > (2 * (long)nums[idx_2]))
                {
                    ans += (end - idx_2);
                    cout << (end - idx_2) << end << idx_2;
                    idx_1 += 1;
                }
                else
                {
                    idx_2 += 1;
                }
            }
        }

        return ans;
    }
};






