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
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2){
        string ans1;
        string ans2;
        for (int i = 0; i < word1.size(); i++)
        {
            ans1 += word1[i];
        }
        for (int i = 0; i < word2.size(); i++)
        {
            ans2 += word2[i];
        }
        return ans1 == ans2;
    }
};