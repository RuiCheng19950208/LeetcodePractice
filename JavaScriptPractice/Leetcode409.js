var longestPalindrome = function(s) {
    let isPlus=false;
    let ans=0;
    let theDict={}
    for(let c of s)
    {
        if (!(c in theDict)) {
            theDict[c]=1;            
        }
        else 
        {
            theDict[c]++;
        }

    }
    for (let key of theDict) {
        if (theDict[key]%2==1) {
            isPlus=true;
        }
        ans+=2*Math.floor(theDict[key]/2);
        
    }


    if (isPlus) {
        ans++;    
    }
    return ans;
};