#include<string>
#include<vector>
class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        vector<int> dp;
        for (int i =0 ; i < s.size()+1; i++)
        {
            dp.push_back(i);
        }
        for(int i = 1; i < dp.size(); i++)
        {
            dp[i] = dp[i-1]+1;
            for(string key : dictionary)
            {
                int ksize= key.size();
                if (ksize<=i)
                {
                    if (s.substr(i-ksize,ksize) == key)
                    {
                        dp[i] = min(dp[i],dp[i-ksize]);
                    }
                }
            }
        }
        return dp[dp.size()-1];
    }
};