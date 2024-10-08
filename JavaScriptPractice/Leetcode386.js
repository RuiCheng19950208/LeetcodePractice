var lexicalOrder = function(n) {

    let ans = [];
    for (let i = 1; i < n+1; i++) {
        ans.push(i)
    }
    
    ans.sort((a,b)=>a.toString().localeCompare(b.toString()))
    return ans
};