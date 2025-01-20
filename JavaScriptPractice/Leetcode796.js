var rotateString = function(s, goal) 
{
    if(s.length!=goal.length){return false;}
    let temp=s+s;
    return temp.includes(goal);
    
};