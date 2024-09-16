#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

using namespace std;

class Solution1672 {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int temp_sum = 0;
        int ans = 0;
        vector<int> sum;
        for (int i=0; i < accounts.size(); i++) {
            for (int j=0; j < accounts[0].size(); j++) {
                temp_sum = temp_sum + accounts[i][j];

            }
            sum.push_back(temp_sum);
            temp_sum = 0;
        }
        ans = *max_element(sum.begin(), sum.end());
        return ans;

    }
};
int main()
{
    Solution1672 s;
    //string a="asdas";
    //string b="asdas";
    /*printf('%d',s.maximumWealth(vector<vector<int>>& a = {}));*/

};