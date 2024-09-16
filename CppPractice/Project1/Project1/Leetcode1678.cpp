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
    string interpret(string command) {

        int index = 0;
        string ans;
        while (index < command.size())
        {
            if (command[index] == 'G')
            {
                ans += "G";
                index += 1;

            }
            else if (command[index] == '(' and command[index + 1] == ')')
            {
                ans += "o";
                index += 2;

            }
            else  if (command[index] == '(' and command[index + 1] == 'a')
            {
                ans += "al";
                index += 4;
            }

        }

        return ans;


    }
};