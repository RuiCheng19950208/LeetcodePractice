class Solution {
public:
    string addBinary(string a, string b) 
    {
        string ans;
        int carry = 0;
        reverse(a.begin(),a.end());
        reverse(b.begin(),b.end());
        int curA=0;
        int curB=0;
        while(curA<a.size()||curB<b.size()||carry)
        {
            int digit1=0;
            int digit2=0;
            if(curA<a.size())
            {
                if(a[curA]=='1'){digit1=1;}else{digit1=0;}
                curA++;
            }
            if(curB<b.size())
            {
                if(b[curB]=='1'){digit2=1;}else{digit2=0;}
                curB++;
            }
            ans+=to_string((digit1+digit2+carry)%2);
            carry = (digit1+digit2+carry)/2;
        }
        reverse(ans.begin(),ans.end());
        return ans;
        
    }
};