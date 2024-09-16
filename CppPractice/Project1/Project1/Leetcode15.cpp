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
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> temp;
        int temp_sum;
        if (nums.size()<3)
        {
            return ans;

        }
        int left;
        int right;
        sort(nums.begin(),nums.end());
        for (int i = 0; i < nums.size()-2; i++)
        {
            if (i!=0 and nums[i-1]==nums[i])
            {
                continue;
            }
            left = i + 1;
            right = nums.size() - 1;
            while (left<right)
            {
                temp_sum = nums[i] + nums[left] + nums[right];
                if (temp_sum == 0)
                {
                    temp = { nums[i],nums[left],nums[right] };
                    ans.push_back(temp);
                    while (nums[left+1]==nums[left] and left+1<right)
                    {
                        left++;
                    }
                    left++;
                    while (nums[right- 1] == nums[right] and right-1>0)
                    {
                        right--;

                    }
                    right--;

                }
                else if (temp_sum<0)
                {
                    left++;

                }
                else if (temp_sum>0)
                {
                    right--;
                }
            }

        }

        return ans;


    }
};