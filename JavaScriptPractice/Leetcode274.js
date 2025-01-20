var hIndex = function(citations) 
{
    let ans=0;
    citations.sort((a,b)=>b-a);
    // citations.reverse();
    for(let i=0;i<citations.length;i++)
    {
        if(citations[i]>=i+1){ans=i+1;}
        else{break;}
    }
    return ans;
};