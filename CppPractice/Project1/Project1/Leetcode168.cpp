
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
    string convertToTitle(int columnNumber) {
        string ans;
        while (columnNumber>0)
        {
            columnNumber--;
            ans += 'A' + (columnNumber % 26);
            columnNumber /= 26;
        }
        reverse(ans.begin(), ans.end());
        return ans;

    }
};