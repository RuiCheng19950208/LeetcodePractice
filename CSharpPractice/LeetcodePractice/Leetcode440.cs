public class Solution440 {
    private long countK(long prefix,long n)
    {
        long ans=0;
        long curPrefix = prefix;
        long nextPrefix = prefix+1;
        while (curPrefix<=n)
        {
            ans+=Math.Min(n+1,nextPrefix) - curPrefix;
            curPrefix*=10;
            nextPrefix*=10;
        }
        return ans;
    }
    public int FindKthNumber(long n, long k) {
        int prefix = 1;
        k -=1;
        while (k>0)
        {
            long count = countK(prefix,n);
            if (count<=k)
            {
                k-=count;
                prefix+=1;
            }
            else
            {
                k-=1;
                prefix*=10;
            }
        }
        return prefix;
    }
}