public class Solution67 {
    public string ReverseString(string s)
    {
        char[] temp = s.ToCharArray();
        Array.Reverse(temp);
        return new string(temp);

    }
    public string AddBinary(string a, string b) 
    {
        a = ReverseString(a);
        b = ReverseString(b);
        List<string> ans=new List<string>();
        // Console.WriteLine(a);
        // Console.WriteLine(b);

        int carry =0;
        int aDigit=0;
        int bDigit=0;
        for(int i=0;i<Math.Max(a.Length,b.Length);i++)
        {
            if(i<a.Length && i<b.Length)
            {
                aDigit = a[i] - '0';
                bDigit = b[i] - '0';
                ans.Add(((aDigit + bDigit + carry)%2).ToString());
                carry = (aDigit + bDigit + carry)/2;
            }
            else if(i<a.Length)
            {
                aDigit = a[i] - '0';
                ans.Add(((aDigit + carry)%2).ToString());
                carry = (aDigit + carry)/2;

            }
            else if(i<b.Length)
            {
                bDigit = b[i] - '0';
                ans.Add((( bDigit + carry)%2).ToString());
                carry = (bDigit + carry)/2;
            }

        }
        if(carry>0){ans.Add("1");}
        // foreach(string e in ans)
        // {
        //     Console.WriteLine(e);
        // }
        ans.Reverse();
        ans.ToArray();
        return string.Join("", ans);
    }
}