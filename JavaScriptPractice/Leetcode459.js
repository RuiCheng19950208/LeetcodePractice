var repeatedSubstringPattern = function(s) 
{
    let ss= s+s;
    let sub = ss.slice(1,ss.length-1);
    return sub.includes(s);
};