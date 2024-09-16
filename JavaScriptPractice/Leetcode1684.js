var countConsistentStrings = function(allowed, words) 
{
    let ans=0;
    let goalSet  = new Set();
    for(const c of allowed)
    {
        goalSet.add(c);
    }
    for(const word of words)
    {
        let tempSet = new Set();
        let isSubset = true;
        for(const c of word)
        {
            tempSet.add(c)
        }
        for(const element of tempSet)
        {
            if(!(goalSet.has(element)))
            {
                isSubset = false;
                break;
            }
        }
        if (isSubset) {
            ans++;
        }
    }
    return ans;
};