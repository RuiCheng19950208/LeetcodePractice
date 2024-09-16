#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

using namespace std;

class Solution {
public:
    string reverseStr(string s, int k) {
        int idx = 0;
        for (size_t i = 0; i < s.size(); i += 2 * k)
        {
            reverse(s.begin() + idx, min(s.begin() + idx + k, s.end()));
            idx += 2 * k;

        }
        return s;


    }
};