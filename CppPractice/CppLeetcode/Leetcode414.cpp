class Solution {
public:
    int thirdMax(vector<int>& nums) {
        // Sort the vector in ascending order
        set<int> theSet(nums.begin(), nums.end());
        
        vector<int> theSetVec(theSet.begin(), theSet.end());
        sort(theSetVec.begin(), theSetVec.end());
        if (theSetVec.size()<3)
        {
            return theSetVec[theSetVec.size()-1];
        }
        else
        {
            return theSetVec[theSetVec.size()-3];
        }
    }
};