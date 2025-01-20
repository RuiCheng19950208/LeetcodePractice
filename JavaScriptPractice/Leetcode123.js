var maxProfit = function(prices) 
{
    let sells = [0,0];
    let buys=[-1000000,-1000000];
    let n = sells.length;
    for(let i=0;i<prices.length;i++)
    {
        for(let j=0;j<n;j++)
        {
            if(j==0){buys[j]=Math.max(buys[j],-prices[i]);}
            else{buys[j]=Math.max(buys[j],sells[j-1]-prices[i]);}
            sells[j] = Math.max(sells[j],buys[j]+prices[i]);
        }
    }
    return sells[n-1];
};