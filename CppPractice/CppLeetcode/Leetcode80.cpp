class Solution {
public:
    int removeDuplicates(vector<int>& nums) 
    {
        int slow = 0;
        unordered_map<int,int> theMap;
        for(int i=0;i<nums.size();i++)
        {
            nums[slow]=nums[i];
            if(theMap.find(nums[i])==theMap.end())
            {
                theMap[nums[i]]=1;
                slow++;
            }
            else if(theMap[nums[i]]==1)
            {
                theMap[nums[i]]+=1;
                slow++;
            }
        }
        return slow;
    }
};