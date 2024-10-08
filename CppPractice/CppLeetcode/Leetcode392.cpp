class Solution {
public:
    bool isSubsequence(string s, string t) {
        int slow=0;
        int fast = 0;
        if(s.size()==0)
        {
            return true;
        }
        if (t.size()==0)
        {
            return false;

        }
        while (fast<t.size())
        {
            if (s[slow]==t[fast])
            {
                slow++;
                fast++;
            }
            else
            {
                fast++
            }
            if(slow>=s.size())
            {
                return false;
            }
            
        }
        return true;
    }
};