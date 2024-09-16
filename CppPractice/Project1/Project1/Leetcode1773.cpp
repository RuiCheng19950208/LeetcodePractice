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
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
		int ans=0;
		int index = 0;
		if (ruleKey=="type")
		{
			index = 0;
			
		}
		else if (ruleKey == "color")
		{
			index = 1;

		}
		else
		{
			index = 2;

		}

		for (int i = 0; i < items.size(); i++)
		{
			if (items[i][index]==ruleValue)
			{
				ans += 1;

			}

		}
		return ans;


    }
};