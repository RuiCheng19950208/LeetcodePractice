class Solution {
public:
    int rob(vector<int>& nums) 
    {
        vector<int> dp = vector<int>(nums.size()+2,0);
        for(int i=2;i<dp.size();i++)
        {
            dp[i]=max(dp[i-1],dp[i-2]+nums[i-2]);
        }
        return dp[dp.size()-1];
    }
};