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
	void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
		if (n == 0)
		{
			return;

		}
		for (int i = m; i < nums1.size(); i++)
		{
			nums1[i] = nums2[i - m];
		}
		sort(nums1.begin(), nums1.end());
	}
};