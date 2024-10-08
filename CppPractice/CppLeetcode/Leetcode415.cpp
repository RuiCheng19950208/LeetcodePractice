class Solution {
public:
    string addStrings(string num1, string num2) {
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        int ptr1=0;
        int ptr2=0;
        int carry = 0;
        string ans ="";
        while (ptr1<num1.size() || ptr2<num2.size1)
        {
            int d1=0;
            int d2=0;
            if (ptr1<num1.size())
            {
                d1 = num1[ptr1]-'0';
                ptr1++;
            }
            if (ptr2<num2.size())
            {
                d2=nums[ptr2]-'0';
                ptr2++;
            }
            ans += to_string((d1+d2+carry)%10);
            carry = (d1+d2+carry)/10;
        }
        if (caryy>0)
        {
            ans+=to_string(carry);
        }
        reverse(ans.begin(), ans.end());
        return ans;
    
    }   
};