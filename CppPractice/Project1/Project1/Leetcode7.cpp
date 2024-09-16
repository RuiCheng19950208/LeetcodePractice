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
    int reverse(int x) {
        if (x>=INT_MAX or x<=INT_MIN)
        {
            return 0;
        }
        bool is_neg;
        string x_str;
        int temp;
        if (x<0)
        {
            temp = -x;
            is_neg = true;
        }
        else
        {
            temp = x;
            is_neg = false;
        }
        x_str = to_string(temp);
        ::reverse(x_str.begin(),x_str.end());
        if (is_neg)
        {
            x_str = "-" + x_str;

        }
        try {
            int ans = stoi(x_str);
            return ans;
        }
        catch (const std::out_of_range& e) {
            return 0;
        }

    }
};