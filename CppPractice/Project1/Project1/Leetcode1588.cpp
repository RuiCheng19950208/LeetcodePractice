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
    int sumOddLengthSubarrays(vector<int>& arr) {
        int temp_len = 1;
        int ans = 0;
        while (temp_len <= arr.size())
        {
            for (int i = 0; i < arr.size() - temp_len + 1; i++)
            {
                for (int j = 0; j < temp_len; j++)
                {
                    ans += arr[i + j];
                }

            }
            temp_len += 2;

        }
        return ans;



    }
};