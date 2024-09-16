public class Solution342 {
    public bool IsPowerOfFour(int n) {
        if (n<=0)
        {
            return false;
        }
        while (n%4==0)
        {
            n=n/4;
        }
        if (n==1)
        {
            return true;
        }
        return false;
    }
}