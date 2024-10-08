var uncommonFromSentences = function(s1, s2) {
    let s1List = s1.split(" ")
    let s2List = s2.split(" ")
    let dict1={}
    let dict2={}
    let res=[]
    for (let i = 0; i < s1List.length; i++) {
        let theKey = s1List[i]
        if (!dict1[theKey]) {
            dict1[theKey] = 1
        }
        else
        {
            dict1[theKey]++
        }
    }
    for (let i = 0; i < s2List.length; i++) {
        let theKey = s2List[i]
        if (!dict2[theKey]) {
            dict2[theKey] = 1
        }
        else
        {
            dict2[theKey]++
        }
    }
    for (let i = 0; i < s1List.length; i++) {
        let theKey = s1List[i]
        if (dict1[theKey]==1 && !dict2.has(theKey)) {
            res.push(theKey)
        }
    }
    for (let i = 0; i < s2List.length; i++) {
        let theKey = s2List[i]
        if (dict2[theKey]==1 && !dict1.has(theKey)) {
            res.push(theKey)
        }
    }
    return res
};