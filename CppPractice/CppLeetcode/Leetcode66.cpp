class Solution {
public:
    vector<int> plusOne(vector<int>& digits) 
    {
        reverse(digits.begin(),digits.end());
        vector<int> ans;
        int carry=0;
        digits[0]++;
        for(int i=0;i<digits.size();i++)
        {
            ans.push_back((carry+digits[i])%10);
            carry = (carry+digits[i])/10;
        }
        if(carry==1){ans.push_back(1);}
        reverse(ans.begin(),ans.end());
        return ans;

        
    }
};