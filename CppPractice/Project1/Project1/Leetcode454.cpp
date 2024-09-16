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
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        map<int, int> target;
        int ans = 0;

        for (int i = 0; i < C.size(); i++)
        {
            for (int j = 0; j < C.size(); j++)
            {
                target[A[i]+B[j]]++;

            }

        }
        for (int i = 0; i < C.size(); i++)
        {
            for (int j = 0; j < C.size(); j++)
            {
                if (target[-(C[i] + D[j])]>0)
                {
                    ans+= target[-(C[i] + D[j])];
                }
            }

        }
        return ans;
    }
};