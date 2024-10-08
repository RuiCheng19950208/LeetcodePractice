var canConstruct = function(ransomNote, magazine) {
    let dictr={}
    let dictm={}
    for (let c of ransomNote) {
        if (dictr[c]) {
            dictr[c]++
        }
        else
        {
            dictr[c]=1
        }
    }
    for (let c of magazine) {
        if (dictm[c]) {
            dictm[c]++
        }
        else 
        {
            dictm[c]=1
        }
    }
    for (let c in dictr) {
        if (dictr[c]>(dictm[c]||0)) {
            return false
        }
    }
    return true
};