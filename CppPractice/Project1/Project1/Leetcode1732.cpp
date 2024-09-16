#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
		int ans=0;
		int temp_h=0;
		for (int i = 0; i < gain.size(); i++)
		{
			temp_h += gain[i];
			ans = max(ans, temp_h);

		}
		return ans;

    }
};