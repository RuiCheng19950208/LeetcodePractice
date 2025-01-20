var arrangeCoins = function(n) 
{
    let left = 0;
    let right = n;
    let mid = 0;
    let temp = 0;
    while(left<=right)
    {
        mid = Math.floor((right+left)/2);
        temp= mid*(mid+1)/2;
        if(temp<n){left=mid+1;}
        else if(temp>n){right=mid-1;}
        else{return mid;}
    }
    return left-1;
};