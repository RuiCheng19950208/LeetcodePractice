
#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

#include <bitset>

#include <numeric>

using namespace std;

class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        map<int, int> dict;
        int target;
        vector<int> exist;
        for (int i = 0; i < deck.size(); i++)
        {
            dict[deck[i]] ++;
        }
     
        for (auto each1:dict)
        {
            for (auto each2 : dict)
            {
                if (gcd(each1.second,each2.second)<2) //gcd accepted by leetcode, no need to write it by self.
                {
                    return false;
                }
            }
        }
        return true;



    }
    int gcd(int a, int b)
    {
        if (b == 0)
            return a;
        return gcd(b, a % b);

    }
};