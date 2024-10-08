class Solution {
public:
    void nextPermutation(vector<int>& nums) 
    {
        int n =nums.size();
        int left = n-2;
        int right  = n-1;
        if(n==1){return;}
        while(nums[left]>=nums[left+1])
        {
            left--;
            if(left==-1){break;}
        }
        if(left>=0)
        {
            while(nums[left]>=nums[right]){right--;}
        }
        if(left>-1){swap(nums[left],nums[right]);}
        reverse(nums.begin()+left+1,nums.end());
        return;        
    }
};