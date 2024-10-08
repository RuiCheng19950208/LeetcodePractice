class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> saved;
        for(int i=0;i<m;i++){saved.push_back(nums1[i]);}
        for(int i=0;i<n;i++){saved.push_back(nums2[i]);}
        sort(saved.begin(),saved.end());
        for(int i=0;i<m+n;i++){nums1[i] = saved[i];}
        
    }
};