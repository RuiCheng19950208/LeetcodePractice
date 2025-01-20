class Solution {
public:
    int longestSquareStreak(vector<int>& nums) 
    {
        unordered_set<int> theSet(nums.begin(),nums.end());
        int ans = 0;
        for(int num:nums)
        {
            int tempAns=1;
            long long cur = num;
            while(cur*cur<=1000000 && theSet.find(cur*cur)!=theSet.end())
            {
                // cout<<cur<<endl;
                cur *= cur;
                tempAns++;
                
            }
            ans=max(ans,tempAns);

        }
        return ans>1?ans:-1;
    }
};