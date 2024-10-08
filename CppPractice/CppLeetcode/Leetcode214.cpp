class Solution {
public:
    vector<int> KMP(string s)
    {
        vector<int> ans(s.size(),0);
        int slow = 0;
        int fast = 1;
        while (fast<s.size())
        {
            if (s[slow]==s[fast])
            {
                slow++;
                ans[fast] = slow;
                fast++;
            }
            else
            {
                if (slow!=0)
                {
                    slow = ans[slow-1];
                }
                else
                {
                    ans[fast]=0;
                    fast++;
                }
            }
        }
        return ans;
    }
    string shortestPalindrome(string s) {
        if (s.size()<=1)
        {
            return s;
        }
        string reverseS = s;
        reverse(reverseS.begin(), reverseS.end());
        string mergedS = s +" "+ reverseS;
        vector<int> KMPList = KMP(mergedS);
        return reverseS.substr(0,reverseS.size() - KMPList[KMPList.size()-1])+s; 
        
    }
};