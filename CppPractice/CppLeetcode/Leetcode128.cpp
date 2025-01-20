class Solution {
public:
    int longestConsecutive(vector<int>& nums) 
    {
        set<int> theSet(nums.begin(),nums.end());
        vector<int> sortedNums(theSet.begin(),theSet.end());
        int ans = 1;
        int temp = 1;
        if(sortedNums.size()==0){return 0 ;}
        if(sortedNums.size()==1){return 1;}
        for(int i=1;i<sortedNums.size();i++)
        {
            if(sortedNums[i]-sortedNums[i-1]==1)
            {
                temp +=1;
                ans = max(ans,temp);
            }
            else
            {temp=1;}

        }
        return ans;
        
    }
};