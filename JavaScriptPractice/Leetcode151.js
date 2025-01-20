var reverseWords = function(s) 
{
    let wordList =[];
    let temp="";
    for(let i=0;i<s.length;i++)
    {
        if(s[i]!=' '){temp+=s[i];}
        else if(temp.length>0)
        {
            wordList.push(temp);
            temp="";
        }
    }
    if(temp.length>0){wordList.push(temp);}
    wordList.reverse();
    return wordList.join(" ");
    
};