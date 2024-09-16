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
    int arrangeCoins(int n) {
        int ans = 0;
        while ((long)ans * (long)ans + ans <= 2 * (long)n) {
            ans++;
        }
        ans--;
        return ans;

    }
};