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
    bool checkPowersOfThree(int n) {
        int exp = 0;
        vector<int> exist;
        while (n > 0)
        {
            if (n > pow(3, exp))
            {
                exp++;

            }
            else if (n == pow(3, exp))
            {
                if (find(exist.begin(), exist.end(), exp) == exist.end())
                {
                    return true;
                }
                else
                {
                    return false;
                }

            }
            else if (n < pow(3, exp))
            {
                if (find(exist.begin(), exist.end(), exp - 1) == exist.end())
                {
                    exist.push_back(exp - 1);
                    n -= pow(3, exp - 1);
                    exp = 0;
                }
                else
                {
                    return false;
                }

            }

        }
        return false;

    }
};
