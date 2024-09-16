#include<string>
#include<vector>
using namespace std;


class Solution {
public:
    int longestIdealString(string s, int k) 
    {
        vector<int> dp(26,0);
        for (char c:s)
        {
            int maxSize=0;
            int index = int(c) - int('a'); //Crutial step to reduce running time
            for (int j = max(0,index-k); j < min(index+k+1,26); j++) //window
            {
                maxSize = max(maxSize,dp[j]);
            }
            dp[index] = maxSize + 1;
        }
        

        

        return *max_element(dp.begin(),dp.end());
    }
};