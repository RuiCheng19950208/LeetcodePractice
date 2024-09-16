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
    int numRabbits(vector<int>& answers) {
        map<int, int> dict;
        int ans = 0;
        int helper = 0;
        for (int i = 0; i < answers.size(); i++)
        {
            dict[answers[i]] += 1;

        }

        for (auto each : dict)
        {
            if (each.first == 0)
            {
                ans += each.second;
            }
            else
            {
                if (each.second % (each.first + 1)>0)
                {
                    helper = 1;

                }
                ans += (helper+(each.second / (each.first + 1))) * (each.first + 1);
            }
            helper = 0;
        }
        return ans;
    }
};