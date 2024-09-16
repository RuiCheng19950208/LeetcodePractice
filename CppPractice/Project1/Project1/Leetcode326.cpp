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
    bool isPowerOfThree(int n) {
        return check_power_3(n, 0);

    }
    bool check_power_3(int n, int e) {
        if (n==pow(3,e))
        {
            return true;

        }
        if (n<pow(3,e))
        {
            return false;
        }
        return check_power_3(n, e + 1);
    }

};