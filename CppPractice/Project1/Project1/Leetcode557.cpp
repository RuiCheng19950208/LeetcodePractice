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
    string reverseWords(string s) {
        int idx;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i]==' ')
            {
                reverse(s.begin()+idx,s.begin()+i);
                idx = i + 1;
            }

        }
        reverse(s.begin() + idx, s.end());


        return s;



    }
};