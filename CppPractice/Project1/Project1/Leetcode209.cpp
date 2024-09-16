#include "LeetcodeHeader.h"

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int fast = 0;
        int slow = 0;
        int temp_sum = nums[0];
        int temp_ans = 1;
        int ans = INT_MAX;
        while (slow!=nums.size()-1)
        {
            if (fast!=nums.size()-1)
            {
                while (temp_sum>target)
                {
                    slow++;
                    temp_sum = temp_sum - nums[slow];
                    temp_ans--;
                }
                fast++;
                temp_sum = temp_sum + nums[fast];
                temp_ans++;
                if (temp_sum>=target)
                {
                    ans = min(ans, temp_ans);
                }
            }
            else
            {
                if (temp_sum-nums[slow]>=target)
                {
                    temp_ans--;
                    temp_sum -= nums[slow];
                    ans = min(ans, temp_ans);
                }
               
                slow++;
            }
            if (ans==1)
            {
                return ans;
            }
        }
        return ans;


    }
};