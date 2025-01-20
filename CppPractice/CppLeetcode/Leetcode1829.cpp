class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) 
    {
        vector<int> ans;
        int theMax = (1<<maximumBit)-1;
        int curXOR=0;
        for(int i=0;i<nums.size();i++)
        {
            if(i==0){curXOR=nums[0];}
            else
            {
                curXOR ^=nums[i];
            }
            ans.push_back(theMax-curXOR);

        }
        reverse(ans.begin(),ans.end());
        return ans;
        
    }
};