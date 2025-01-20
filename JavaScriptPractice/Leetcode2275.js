var largestCombination = function(candidates) 
{
    let ans=0;
    let temp=0;;
    for(let i=0;i<32;i++)
    {
        temp=0;
        for(let num of candidates)
        {
            if(num&(1<<i)){temp++;}
        }
        ans=Math.max(ans,temp);
    }
    return ans;
    
};