class NumArray {
public:
    vector<int> theSumList;
    
    NumArray(vector<int>& nums) {
        int curSum = 0;
        theSumList.push_back(0);
        for(int i = 0; i < nums.size(); i++)
        {   
            curSum +=nums[i];
            theSumList.push_back(curSum);
        }   
    }
    int sumRange(int left, int right) {
        return theSumList[right+1] - theSumList[left];
    }
};
