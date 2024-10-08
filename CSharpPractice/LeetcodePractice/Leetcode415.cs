public class Solution415 {
    public string AddStrings(string num1, string num2) {
        string ans="";
        int ptr1 = num1.Length-1;
        int ptr2 = num2.Length-1;
        int carry=0;
        while (ptr1>=0||ptr2>=0||carry>0)
        {
            int d1=0;
            int d2=0;
            if (ptr1>=0)
            {
                d1 = num1[ptr1--]-'0';   
            }
            if (ptr2>=0)
            {
                d2 = num2[ptr2--]-'0';   
            }
            ans += ((d1+d2+carry)%10).ToString();
            carry = (d1+d2+carry)/10;
        }
        string reverseAns = new string(ans.Reverse().ToArray());
        return reverseAns;
    }
}