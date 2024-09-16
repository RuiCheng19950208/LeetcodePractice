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
    string defangIPaddr(string address) {
        string ans;
        for (int  i = 0; i < address.size(); i++)
        {
            if (address[i]!='.')
            {
                ans += address[i];

            }
            else 
            {
                ans +="[.]";
            
            }
        }

        return ans;



    }
};