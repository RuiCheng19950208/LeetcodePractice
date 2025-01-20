var compressedString = function(word) 
{
    let count=1;
    let curChar = word[0];
    let ans=[];
    if(word.length<2){return "1"+word;}
    for(let i=1;i<word.length;i++)
    {
        if(curChar==word[i])
        {
            if(count==9)
            {
                ans.push("9");
                ans.push(curChar);
                count=1;
            }
            else{count+=1}
        }
        else
        {
            ans.push(String(count));
            ans.push(curChar);
            curChar = word[i];
            count =1;
        }
    }
    ans.push(String(count));
    ans.push(curChar);
    return ans.join("");
};