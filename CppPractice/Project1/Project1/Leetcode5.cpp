
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
    string longestPalindrome(string s) {
        vector<vector<bool>> dp(s.size(), vector<bool>(s.size(), true));
        vector<int> ans(2, 0);
        int max_len = 0;
        for (int j = 0; j < s.size(); j++)
        {
            for (int i = 0; i <= j; i++)
            {
                if (s[i] == s[j])
                {
                    if (j - i < 2)
                    {
                        dp[i][j] = true;
                        if (j - i > max_len - 1)
                        {
                            max_len = j - i + 1;
                            ans = { i,j };
                        }
                    }
                    else
                    {
                        dp[i][j] = dp[i + 1][j - 1];
                        if (dp[i][j])
                        {
                            if (j - i > max_len - 1)
                            {
                                max_len = j - i + 1;
                                ans = { i,j };
                            }

                        }

                    }
                }
                else
                {
                    dp[i][j] = false;
                }

            }

        }
        //cout << ans[0] << ans[1];
        return s.substr(ans[0], ans[1] - ans[0] + 1);


    }
};