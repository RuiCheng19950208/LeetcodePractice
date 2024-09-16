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
    uint32_t reverseBits(uint32_t n) {
        bitset<32> nBits(n);

        for (int i = 0; i < nBits.size() / 2; i++) {
            int temp = nBits[i];
            nBits[i] = nBits[nBits.size() - 1 - i];
            nBits[nBits.size() - 1 - i] = temp;
        }

        int rev = nBits.to_ulong();

        return rev;
    }
};