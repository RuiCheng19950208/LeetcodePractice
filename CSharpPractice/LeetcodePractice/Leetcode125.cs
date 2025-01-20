public class Solution125 {
    public bool IsPalindrome(string s) 
    
    {
        if(s.Length <=1){return true;}
        int left =0;
        int right = s.Length-1;
        while(left<right)
        {
            while(left<=s.Length-1 && !char.IsLetterOrDigit(s[left]))
            {
                left++;
            }
            while(right>=0 && !char.IsLetterOrDigit(s[right]))
            {
                right--;
            }
            if( left<right && char.ToLower(s[right])!=char.ToLower(s[left]))
            {
                return false;
            }
            right--;
            left++;
        }
        return true;
    }
}