class Solution {
public:
    int minSubarray(vector<int>& nums, int p) 
    {
        long long theSum = accumulate(nums.begin(),nums.end(),static_cast<long long>(0)); //cs and js? how to accumulate
        long long goal = theSum%p;
        if(goal==0){return 0;}

        unordered_map<int,int> theMap = {{0,-1}};
        long long cur = 0;
        long long target = 0;
        int n = nums.size();
        int ans = n;
        for(int i=0;i<n;i++)
        {
            cur=(cur+nums[i])%p;
            target = (cur+p-goal)%p;
            if(theMap.find(target)!=theMap.end()){ans=min(ans,i-theMap[target]);}
            theMap[cur] = i;
        }
        return ans==n?-1:ans;
    }
};