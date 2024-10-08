var minExtraChar = function(s, dictionary) {
    let dp= Array.from({length: s.length+1}, (_, i) => i)
    for (let i = 1; i < dp.length; i++) {
        dp[i]=dp[i-1]+1;
        for (let key of dictionary) {
            let lenk = key.length
            if (lenk<=i) {
                if (key==s.substring(i-lenk,i)) {
                    dp[i] = Math.min(dp[i],dp[i-lenk])
                }
            }
        }
    }
    return dp[dp.length-1]
    
};