class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int slow = 0;
        int ans= 1;
        if(nums.size()==1){return 1;}
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]!=nums[slow]){slow++;nums[slow]=nums[i];ans++;}
        }
        return ans;
    }
};