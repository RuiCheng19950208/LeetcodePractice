public class Solution66 {
    public int[] PlusOne(int[] digits) 
    {
        List<int> digitList = new List<int>();
        int place =0;
        int curDigit=0;
        Array.Reverse(digits);
        digits[0]++;
        foreach(int num in digits)
        {
            curDigit = (place + num )%10;
            place =  (place + num) /10;
            digitList.Add(curDigit);
        }
        if(place>0){digitList.Add(1);}
        digitList.Reverse();
        int[] ans = digitList.ToArray();
        return ans;
    }
}