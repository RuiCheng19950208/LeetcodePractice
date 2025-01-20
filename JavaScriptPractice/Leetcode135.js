var candy = function(ratings) 
{
    let ans = new Array(ratings.length).fill(1);
    for(let i=1;i<ratings.length;i++)
    {
        if(ratings[i]>ratings[i-1]){ans[i]=ans[i-1]+1;}
    }
    for(let i=ratings.length-2;i>=0;i--)
    {
        if(ratings[i]>ratings[i+1]){ans[i]=Math.max(ans[i],ans[i+1]+1);}
    }
    return ans.reduce((accu,cur)=>accu+cur,0);
};