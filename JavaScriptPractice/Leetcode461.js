var hammingDistance = function(x, y) 
{
    let temp= x^y;
    let ans=0;
    while(temp>0)
    {
        if(temp%2==1){ans++;}
        temp>>=1;
    }
    return ans;
};