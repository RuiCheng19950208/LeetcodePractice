public class Solution231 {
    public bool IsPowerOfTwo(int n) 
    {
        List<int> tempAns = new List<int>();
        int curNum = 1;
        if (n<=0)
        {
            return false;
        }
        for(int i=0;i<32;i++)
        {
            tempAns.Add(curNum);
            curNum *=2;
        }
        return tempAns.Contains(n);
    }
}