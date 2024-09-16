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
    string addBinary(string a, string b) {

        int a_idx = a.size()-1;
        int b_idx = b.size() - 1;
        int carry=0;
        int temp_sum;
        string ans;
        while (a_idx>=0 or b_idx>=0)
        {   
            temp_sum = 0;
            if (a_idx>=0)
            {
                temp_sum += a[a_idx] - '0';
            }
            if (b_idx >= 0)
            {
                temp_sum += b[b_idx] - '0';
            }
            ans += to_string((carry + temp_sum) % 2);
            if (temp_sum+carry>=2)
            {
                carry = 1;
            }
            else
            {
                carry = 0;
            }
            a_idx--;
            b_idx--;
         

        }
        if (carry==1)
        {
            ans+= to_string(carry);
        }
        reverse(ans.begin(), ans.end());
        return ans;
     
    }
};

//int main()
//{
//    Solution67 s;
//    //string a="asdas";
//    //string b="asdas";
//    printf(s.addBinary("asdas", "asdas").c_str());
//    printf(s.addBinary("asdas", "asdas").c_str());
//
//};