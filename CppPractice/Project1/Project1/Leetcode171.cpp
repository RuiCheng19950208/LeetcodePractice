#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

using namespace std;


class Solution {
public:
    int titleToNumber(string columnTitle) {
        int ans = 0;
        for (int i = columnTitle.size() - 1; i >= 0; i--)
        {
            ans += pow(26, columnTitle.length() - 1 - i) * (columnTitle[i] - 'A' + 1);
        }
        return ans;

    }
};