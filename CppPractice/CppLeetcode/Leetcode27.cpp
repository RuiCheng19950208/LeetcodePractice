class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int ans=0;
        int left = 0;
        int right = nums.size()-1;
        if(nums.size()==0){return 0;}
        while(left<nums.size() && nums[left]!=val)
        {
            left++;
            ans++;
        }
        while(right>=0 && nums[right]==val)
        {
            right--;
        }
        while(left<right)
        {
            swap(nums[left],nums[right]);
            while(left<nums.size() && nums[left]!=val)
            {
                left++;
                ans++;
            }
            while(right>=0 && nums[right]==val)
            {
                right--;
            }
        }
        return ans;
    }
};