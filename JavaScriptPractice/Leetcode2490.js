var isCircularSentence = function(sentence) 
{
    let sList = sentence.split(" ");
    let n = sList.length;
    for(let i=0;i<n-1;i++)
    {
        if(sList[i][sList[i].length-1]!=sList[i+1][0]){return false;}
    }
    if(sList[n-1][sList[n-1].length-1]!=sList[0][0]){return false;}
    return true;
};