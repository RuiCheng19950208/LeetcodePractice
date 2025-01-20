var maxProfit = function(k, prices) 
{
    let sells=[];
    let buys=[];
    for(let i=0;i<k;i++)
    {
        sells.push(0);
        buys.push(-100000);
    }
    for(let i=0;i<prices.length;i++)
    {
        for(let j=0;j<k;j++)
        {
            if(j==0){buys[j]=Math.max(buys[j],-prices[i]);}
            else{buys[j]=Math.max(buys[j],sells[j-1]-prices[i]);}
            sells[j]=Math.max(sells[j],buys[j]+prices[i]);
        }
    }
    return sells[k-1];
};