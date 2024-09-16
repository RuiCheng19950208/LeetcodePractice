var countBits = function(n) {
    let dp = Array(n+1).fill(0)
    if (n==0) {
        return dp
    }
    dp[1]=1
    for (let i = 1; i < dp.length; i++) {
        if (i%2==0) {
            dp[i] = dp[i/2]
        }
        else 
        {
            dp[i] = dp[Math.floor(i/2)]+1
        }
    }
};