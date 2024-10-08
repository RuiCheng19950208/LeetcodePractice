var minSubarray = function(nums, p) 
{
    let theSum = nums.map(num=>num%p).reduce((arr,num)=>arr+num,0)%p;
    let n= nums.length;
    let ans = n ;
    let cur = 0;
    let target =0;
    let theDict = new Map([[0,-1]]);
    if(theSum==0){return 0;}

    for(let i=0;i<n;i++)
    {
        cur = (cur+nums[i])%p;
        target = (cur+p-theSum)%p;
        if(theDict.has(target))
        {
            ans=Math.min(ans,i-theDict.get(target));
        }
        theDict.set(cur,i);

    }
    return ans==n?-1:ans;
    
};