#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

#include <bitset>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> num_merge;
        num_merge.insert(num_merge.end(), nums1.begin(), nums1.end());
        num_merge.insert(num_merge.end(), nums2.begin(), nums2.end());
        sort(num_merge.begin(), num_merge.end());
        if (num_merge.size()%2==1)
        {
            return (double)num_merge[num_merge.size() / 2];

        }
        else
        {
            return ((double)num_merge[num_merge.size() / 2]+ (double)num_merge[num_merge.size() / 2-1])/2;

        }

    }
};