class Solution349 {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        set<int> set1(nums1.begin(),nums1.end());
        set<int> set2(nums2.begin(), nums2.end());
        for(int e:set1)
        {
            if(set2.find(e) != set2.end())
            {
                res.push_back(e);
            }   
        }
        return res;
    }
};