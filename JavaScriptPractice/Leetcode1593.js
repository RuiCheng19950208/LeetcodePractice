let theSet;
let n;
let theS;
var helper = function(start)
{
    if(start==n){return theSet.size;}
    let ans=0;
    for(let end=start+1;end<n+1;end++)
    {
        let curString = theS.slice(start,end);
        if(!theSet.has(curString))
        {
            theSet.add(curString);
            ans=Math.max(ans,helper(end));
            theSet.delete(curString);
        }
    }
    return ans;
}
var maxUniqueSplit = function(s) 
{
    theS=s;
    n=s.length;
    theSet = new Set();
    return helper(0);  
};