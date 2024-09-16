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
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0)
        {
            return 0;
        }
        map<char, int> dict;
        int fast = 0;
        int slow = 0;
        int ans = 1;
        dict[s[slow]]++;

        while (fast < s.size() - 1)
        {
            fast++;
            dict[s[fast]]++;
            while (dict[s[fast]] > 1)
            {
                dict[s[slow]]--;
                slow++;
            }

            ans = max(ans, fast - slow + 1);


        }
        return ans;
    }
};