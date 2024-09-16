
var generateParenthesis = function(n) 
{
    let deque = [];
    let right = 0;
    let left = 0;
    let tempString = "";
    let res = [];

    deque.push([0,0,""]);
    while (deque.length>0) 
    {
        let tuple = deque.shift();
        left = tuple[0];
        right = tuple[1];
        tempString = tuple[2];
        // console.log(tuple)
        if (left==n && right==n) {
            res.push(tempString)
        }
        if (left<n) {
            deque.push([left+1,right,tempString+"("]);
            
        }
        if (left>right) {
            deque.push([left,right+1,tempString+")"]);
        }
    }
    return res;
};