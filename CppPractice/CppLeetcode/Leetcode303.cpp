class NumArray {
public:
    vector<int> publicNums;
    NumArray(vector<int>& nums) {
        publicNums = nums;
    }
    
    int sumRange(int left, int right) {
        int theSum  = accumulate(publicNums.begin()+left, publicNums.begin()+right+1, 0);
        return theSum;
        
    }
};