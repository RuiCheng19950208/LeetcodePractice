class Solution {
public:
    string multiply(string num1, string num2) 
    {
        
        vector<int> ans(num1.size()+num2.size(),0);
        reverse(num1.begin(),num1.end());
        reverse(num2.begin(),num2.end());
        for(int i=0;i<num1.size();i++)
        {
            for(int j=0;j<num2.size();j++)
            {
                int d1=num1[i]-'0';
                int d2 =num2[j]-'0';
                ans[i+j] += d1*d2;
            }
        }
        int carry = 0;
        string ansString;
        for(int i=0;i<ans.size();i++)
        {
            ans[i]+=carry;
            carry = ans[i]/10;
            ans[i] = ans[i]%10;
            ansString += to_string(ans[i]);
        }
        int lenAns = ans.size();
        for(int i=ans.size()-1;i>=0;i--)
        {
            if(ans[i]==0){lenAns--;}else{break;}
        }
        ansString = ansString.substr(0,lenAns);
        reverse(ansString.begin(),ansString.end());
        if(ansString.size()==0){return "0";}
        return ansString;
        
        
    }
};