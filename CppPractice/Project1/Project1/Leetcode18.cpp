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
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
                
        vector<vector<int>> ans;
        vector<int> temp;
        int temp_sum;
        int left;
        int right;
        if (nums.size()<4)
        {
            return ans;
        }
        sort(nums.begin(),nums.end());
        for (int i = 0; i < nums.size()-3; i++)
        {
            if (i!=0 and nums[i]==nums[i-1])
            {
                continue;
            }
            for (int j = i+1; j < nums.size() - 2; j++)
            {
                if (j-1!=i and nums[j] == nums[j-1])
                {
                    continue;
                }
                left = j + 1;
                right = nums.size() - 1;
                while (left<right)
                {
                    temp_sum = nums[j] + nums[left] + nums[right];
                    if (temp_sum == target - nums[i])
                    {
                        temp = { nums[i],nums[j],nums[left],nums[right] };
                        ans.push_back(temp);
                        while (nums[left+1]==nums[left] and left+2<right)
                        {
                            left++;

                        }
                        left++;
                        while (nums[right -1] == nums[right] and right-1>0)
                        {
                            right--;

                        }
                        right--;

                    }
                    else if (temp_sum < target - nums[i])
                    {
                        left++;
                    }
                    else 
                    {
                        right--;

                    }
                }
            }
        }
        return ans;

    }
};