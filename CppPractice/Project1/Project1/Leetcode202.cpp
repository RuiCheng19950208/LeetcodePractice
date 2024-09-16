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
    bool isHappy(int n) {
        int temp_sum = 0;
        int temp_n = n;
        int remain;
        vector<int> exist;
        while (n > 0)
        {
            // cout << n <<"  "; 

            while (temp_n > 0)
            {
                remain = temp_n % 10;
                temp_n = temp_n / 10;
                temp_sum += pow(remain, 2);

            }
            if (temp_sum == 1)
            {
                return true;
            }
            else if (find(exist.begin(), exist.end(), temp_sum) != exist.end())
            {



                return false;

            }
            exist.push_back(temp_sum);

            n = temp_sum;

            temp_sum = 0;
            temp_n = n;
        }
        return false;
    }
};