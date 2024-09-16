#include<vector>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) 
    {
        int curRight = 0;
        int maxRight = 0;
        int step = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (i>curRight)
            {
                step++;
                curRight = maxRight;
            }
            
            if (maxRight<i+nums[i])
            {
                maxRight = i+nums[i];
                if (maxRight >=nums.size()-1 && i<nums.size()-1)
                {
                    return step+1;
                }
            }
            // cout<<i<<" "<<curRight<<" "<<maxRight<<endl;
            
        }
        return step;
        
    }
};