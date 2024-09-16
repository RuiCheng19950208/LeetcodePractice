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
    int binaryGap(int n) {
        bitset<32> b_n(n);
        int slow = 0;
        int fast = 0;
        int ans = 0;
        int temp_ans = 0;
        for (int i = 0; i < b_n.size() - 1; i++)
        {
            if (b_n[slow] != 1)
            {
                slow++;
            }
            else
            {
                break;
            }
        }
        if (slow >= b_n.size() - 1)
        {
            return 0;
        }
        fast = slow;
        for (int i = slow + 1; i < b_n.size(); i++)
        {
            if (b_n[fast] != 1)
            {
                fast++;
            }
            else
            {
                break;
            }
        }
        if (fast >= b_n.size())
        {
            return 0;
        }
        ans = fast - slow;
        slow = fast;
        while (fast < b_n.size() - 1)
        {
            fast++;
            temp_ans++;
            if (b_n[fast] == 1)
            {
                ans = max(ans, temp_ans);
                slow = fast;
                temp_ans = 0;

            }

        }
        return ans;


    }
};