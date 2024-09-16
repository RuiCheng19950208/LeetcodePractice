#include <vector>
using namespace std;
class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> stack={-1};
        int ans = 0;
        for(int i = 0; i < s.size(); i++)
        {
            if(s[i]=='(')
            {
                stack.push_back(i);
            }
            else
            {
                stack.pop_back();
                if(stack.size()==0)
                {
                    stack.push_back(i);
                }
                else
                {
                    ans= max(ans,i-stack[stack.size()-1]);
                }   
            }
        }
        return ans;
    }
};