class Solution {
private:
    int countK(int prefix, int n)
    {
        int curPrefix = prefix;
        int nextPrefix = prefix+1;
        int ans = 0;
        while (curPrefix<=n)
        {
            ans += Math.min({n+1,nextPrefix}) - curPrefix;
            curPrefix *=10;
            nextPrefix *=10;
        }
        return ans
    }
public:
    int findKthNumber(int n, int k) {
        int prefix = 1;
        k -=1 ;
        while (k>0)
        {
            int curCount = countK(prefix,n);
            if (curCount<=k)
            {
                k-=curCount;
                prefix +=1;
            }
            else
            {
                k-=1;
                prefix *=10;
            }

            
        }
        return prefix;
        
    }
};