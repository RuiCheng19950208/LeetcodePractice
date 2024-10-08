var isSubsequence = function(s, t) {
    let slow=0;
    let fast=0;
    if (s.length==0) {
        return true
    }
    if (t.length==0) {
        return false
    }
    while (fast<t.length) {
        if (s[slow]==t[fast]) {
            fast++
            slow++
        }
        else 
        {
            fast++
        }
        if (slow>=s.length) {
            return true
        }
        
    }
    return false
};