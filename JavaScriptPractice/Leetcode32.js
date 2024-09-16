var longestValidParentheses = function(s) {
    let ans=0
    let stack=[-1]
    for (let i = 0; i < s.length; i++) {
        if (s[i]=="(") {
            stack.push(i)
        }
        else 
        {
            stack.pop()
            if (stack.length==0) {
                stack.push(i)
            }
            else 
            {
                ans=math.max(ans,i-stack[stack.length-1])
            }
        }
        
    }
    return ans
    
};