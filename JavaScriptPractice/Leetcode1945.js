var getLucky = function(s, k) 
{
    let ans = "";
    for (const c of s) 
    {
        ans += c.charCodeAt(0) - 'a'.charCodeAt(0) +1;
    }
    console.log(ans);
    while (k>0) {
        ans = ans.toString().split('').reduce((accu,c)=>{return accu +parseInt(c);},0).toString();
        k--;
    }
    return parseInt(ans);
};