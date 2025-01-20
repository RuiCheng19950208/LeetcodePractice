public class Solution274 {
    public int HIndex(int[] citations) 
    {
        int ans=0;
        Array.Sort(citations);
        Array.Reverse(citations);
        for(int i=0;i<citations.Length;i++)
        {
            if(citations[i]>=i+1){ans=i+1;}
            else{break;}
        }
        return ans;
    }
}