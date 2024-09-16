#include "LeetcodeHeader.h"

class Solution {
public:
    vector<string> ans;
    void helper(int n, int len_temp_string, string temp_string, int open) 
    {
        if (len_temp_string ==2*n and open==0)
        {
            ans.push_back(temp_string);
        }
        if (open<0 or open>=n or len_temp_string > 2 * n)
        {
            return;
        }
        helper(n, len_temp_string + 1, temp_string + "(", open + 1);
        helper(n, len_temp_string + 1, temp_string + ")", open - 1);
    
    
    }
    vector<string> generateParenthesis(int n) {
        helper(n,0,"",0);
        return ans;

    }
};