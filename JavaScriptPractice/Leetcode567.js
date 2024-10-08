function dictEqual(d1,d2)
{
    for(let [key,val] of d1)
    {
        if(d2.get(key)!=val){return false;}
    }
    return true;
}
var checkInclusion = function(s1, s2) {
    let s1len = s1.length;
    let s2len = s2.length;
    if(s1len>s2len){return false;}
    let s1Map = new Map();
    let tempMap = new Map();
    for (let c='a';c<='z';c=String.fromCharCode(c.charCodeAt(0)+1))
    {
        s1Map.set(c,0); 
    }
    for(let c of s1){s1Map.set(c,s1Map.get(c)+1);}
    for (let c='a';c<='z'; c=String.fromCharCode(c.charCodeAt(0)+1))
    {
        tempMap.set(c,0);
    }

    for(let c of s2.substring(0,s1len)){tempMap.set(c,tempMap.get(c)+1);}
    let fast = s1len-1;
    for(let i=0;i<s2len-s1len;i++)
    {
        // for(let [key,val] of tempMap){console.log(key,val);}
        if(dictEqual(tempMap,s1Map)){return true;}
        fast++;
        if(fast<s2len)
        {
            tempMap.set(s2[fast],tempMap.get(s2[fast])+1);
            tempMap.set(s2[i],tempMap.get(s2[i])-1);
        }
    }
    if(dictEqual(tempMap,s1Map)){return true;}else{return false;}

};