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
    int minIncrementForUnique(vector<int>& A) {
        sort(A.begin(), A.end());
        int ans = 0;
        int pre = 0;
        int cur = 0;
        for (int i = 1; i < A.size(); i++)
        {
            pre = A[i - 1];
            cur = A[i];
            if (pre>=cur)
            {
                A[i] = pre + 1;
                ans += pre - cur + 1;

            }

        }
        return ans;
    }
};