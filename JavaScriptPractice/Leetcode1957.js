var makeFancyString = function(s) {

    if(s.length<3){return s;}
    let ans=s[0]+"";
    let temp=1;
    let curChar =s[0];
    for(let i=1;i<s.length;i++)
    {
        if(curChar==s[i])
        {
            temp+=1;
            if(temp<3)
            {
                ans+=s[i];
            }
        }
        else
        {
            temp=1;
            curChar =s[i];
            ans+=s[i];

        }
    }
    return ans;
    
};