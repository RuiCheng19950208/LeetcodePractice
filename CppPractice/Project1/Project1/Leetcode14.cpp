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
    string longestCommonPrefix(vector<string>& strs) {
        int min_len = INT_MAX;
        string ans = "";
        if (strs.size()==0)
        {
            return ans;
        }
        for (int i = 0; i < strs.size(); i++)
        {
            if (strs[i].size()<min_len)
            {
                min_len = strs[i].size();
            }

        }
        for (int i = 0; i < min_len; i++)
        {
            for (int j = 1; j < strs.size(); j++)
            {
                if (strs[j][i]==strs[j-1][i])
                {

                }
                else
                {
                    return ans;
                }

            }
            ans += strs[0][i];

        }
        return ans;

    }
};