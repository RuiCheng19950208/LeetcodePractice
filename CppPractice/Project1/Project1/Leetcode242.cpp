
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
    bool isAnagram(string s, string t) {
        sort(s.begin(),s.end());
        sort(t.begin(), t.end());
        return s == t;

    }
};