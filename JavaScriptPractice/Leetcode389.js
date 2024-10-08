var findTheDifference = function(s, t) {
    let dictt={}
    let dicts={}
    for (let c of s) {
        if (dicts[c]) {
            dicts[c]++
        }
        else 
        {
            dicts[c]=1
        }
        
    }
    for (let c of t) {
        if (dictt[c]) {
            dictt[c]++
        }
        else 
        {
            dictt[c]=1
        }
    }
    for (let c of t) {
        if (!dicts[c]|| dictt[c]>dicts[c]) {
            return c;
        }
    }
    return '0'

    
};