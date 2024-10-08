var minLength = function(s) 
{
    let n = s.length;
    let theStack = []
    for(let i=0;i<n;i++)
    {
        if((s[i]=='B'&&theStack[theStack.length-1]=='A')||(s[i]=='D'  &&theStack[theStack.length-1]=='C'))
        {
            theStack.pop();
        }
        else
        {
            theStack.push(s[i]);
        }
    }

    return theStack.length;
    
};