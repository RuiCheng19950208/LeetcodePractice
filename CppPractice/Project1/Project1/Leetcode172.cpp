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
    int trailingZeroes(int n) {
        int exp = 1;
        int ans = 0;
        while (pow(5, exp) <= n) {
            ans += n / pow(5, exp);
            exp++;
        }
        return ans;
    }
};