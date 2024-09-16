#include <vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) 
    {
        
        if (nums.size()==1)
        {
            return nums[0];
            
        }
        int curMax = nums[0];
        int res = curMax;
        for (int i = 1; i < nums.size(); i++)
        {
            curMax = max(curMax+nums[i],nums[i]);
            res =max(res,curMax);

        }
        return res;
    }
};