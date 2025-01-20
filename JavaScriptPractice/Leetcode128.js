var longestConsecutive = function(nums) 
{
    let theList = [...new Set(nums)];
    theList.sort((a,b)=>a-b);
    let ans=1;
    let temp=1;
    if (theList.length==0){return 0;}
    if (theList.length==1){return 1;}
    for(let i=1;i<theList.length;i++)
    {
        if(theList[i]-theList[i-1]==1){temp+=1;ans=Math.max(ans,temp);}
        else{temp=1;}
    }
    return ans;
};