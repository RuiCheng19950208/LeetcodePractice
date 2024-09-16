
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
    int minOperations(int n) {
        int half = n / 2;
        int ans=0;
        if (n%2==0)
        {
            for (int i = 0; i < half; i++)
            {
                ans += (1 + 2 * i);

            }
        }
        else
        {
            for (int i = 0; i < half; i++)
            {
                ans += (2 + 2 * i);

            }
        }
        return ans;

    }
};