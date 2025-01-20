var longestSquareStreak = function(nums) {
    nums.sort((a,b)=>a-b);
    let theSet = new Set(nums);
    let ans=0;
    for (let num of nums)
    {
        let cur = num*num;
        let tempAns = 1;
        while(theSet.has(cur))
        {
            tempAns++;
            cur *=cur;
        }
        ans = Math.max(ans,tempAns);
    }
    return ans>1?ans:-1;

};