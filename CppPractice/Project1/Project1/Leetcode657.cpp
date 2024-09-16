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
    bool judgeCircle(string moves){
        vector<int> ans(2,0);
        for (char each:moves)
        {
            if (each=='U')
            {
                ans[0] -= 1;

            }
            else if (each == 'D')
            {
                ans[0] += 1;
            }
            else if (each == 'R')
            {
                ans[1] += 1;
            }
            else
            {
                ans[1] -= 1;
            }
        }
        return (ans[0] == 0 and ans[1] == 0);


    }
};