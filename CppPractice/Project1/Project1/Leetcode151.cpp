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
        string temp = "";
        string ans;
        vector<string> word_list;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == ' ')
            {
                if (temp.size() > 0)
                {
                    word_list.push_back(temp);
                    temp = "";

                }

            }
            else
            {
                temp += s[i];
            }

        }
        if (temp.size() > 0)
        {
            word_list.push_back(temp);
        }

        reverse(word_list.begin(), word_list.end());
        for (string each : word_list)
        {
            ans += (each + " ");

        }
        ans.pop_back();
        return ans;


    }
};