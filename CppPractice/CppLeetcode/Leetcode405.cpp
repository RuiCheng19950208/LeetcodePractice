class Solution {
public:
    string toHex(int num) {
        if(num==0)
        {
            return "0";
        }
        string ans;
        int digit=0;
        unsigned int n = num;
        while(n>0)
        {
            int digit = n%16;
            n = n/16;
            if(digit<10)
            {
                ans+=digit+'0';
            }
            else
            {
                ans += (digit-10+'a');
            }
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};