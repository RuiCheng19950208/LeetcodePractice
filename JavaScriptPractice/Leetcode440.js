var countK=function(prefix,n){
    let curPrefix = prefix
    let nextPrefix = prefix+1
    let ans=0;
    while (curPrefix<=n) {
        ans+=Math.min(n+1,nextPrefix) - curPrefix
        curPrefix*=10
        nextPrefix*=10
    }
    return ans

};
var findKthNumber = function(n, k) {
    let ans=0
    k-=1
    while (k>0) {
        let count = countK(ans,n)
        if (count<=k) {
            k-=count
            ans+=1
        }
        else 
        {
            k-=1
            ans*=10
        }
    }
    return ans
};