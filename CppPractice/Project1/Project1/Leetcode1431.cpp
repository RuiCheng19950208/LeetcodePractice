#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max_val = *max_element(candies.begin(), candies.end());
        vector<bool> ans;
        for (int i=0; i < candies.size();i++) {
            if (candies[i]+extraCandies>=max_val) {
                ans.push_back(true);
            
            }
            else { ans.push_back(false); }

        }
        return ans;
    }
};
