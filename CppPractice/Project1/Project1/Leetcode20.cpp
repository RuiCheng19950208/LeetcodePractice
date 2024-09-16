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
    bool isValid(string s) {
        vector<char> signal;
        if (s.size()==0)
        {
            return true;
        }
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i]=='(')
            {
                signal.push_back(')');

            }
            else if (s[i]=='[')
            {
                signal.push_back(']');
            }
            else if (s[i] == '{')
            {
                signal.push_back('}');
            }
            else if (s[i] == ')')
            {
                if (signal.size()==0 or signal.back()==')')
                {
                    signal.pop_back();
                }
                else
                {
                    return false;
                }

            }
            else if (s[i] == ']')
            {
                if (signal.size() == 0 or signal.back() == ']')
                {
                    signal.pop_back();
                }
                else
                {
                    return false;
                }


            }
            else if (s[i] == '}')
            {
                if (signal.size() == 0 or signal.back() == '}')
                {
                    signal.pop_back();
                }
                else
                {
                    return false;
                }

            }

        }
        if (signal.size()==0)
        {
            return true;
        }

        return false;

    }
};