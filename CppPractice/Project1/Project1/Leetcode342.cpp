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
    bool isPowerOfFour(int n) {
        bitset<32> bn(n);
        int count = 0;
        int count_all = 0;
        for (int i = 0; i < bn.size(); i += 2)
        {
            if (bn[i] == 1)
            {
                count += 1;
            }

        }

        for (int i = 0; i < bn.size(); i++)
        {
            if (bn[i] == 1)
            {
                count_all += 1;
            }

        }
        return count == 1 and count_all == 1 and n > 0;

    }
};