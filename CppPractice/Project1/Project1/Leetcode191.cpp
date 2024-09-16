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
    int hammingWeight(uint32_t n) {
        bitset<32> bn((int)n);
        int ans = 0;
        for (size_t i = 0; i < bn.size(); i++)
        {
            if (bn[i] == 1)
            {
                ans += 1;

            }

        }
        return ans;
    }
};