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
    bool isPowerOfTwo(int n) {
        bitset<32> b_n(n);
        int count = 0;
        for (int i = 0; i < b_n.size(); i++)
        {
            if (b_n[i] == 1)
            {
                count++;
            }

        }
        return n > 0 and count == 1;


    }
};