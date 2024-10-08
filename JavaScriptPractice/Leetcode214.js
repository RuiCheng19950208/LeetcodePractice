var KMP = function(s)
{
    let fast=1
    let slow=0
    let ans=Array.from({length: s.length}, () => 0)
    while (fast<s.length) {
        if (s[fast]==s[slow]) {
            slow++
            ans[fast]=slow
            fast++
        }
        else 
        {
            if (slow!=0) {
                slow = ans[slow-1]
            }
            else 
            {
                ans[fast]=0
                fast++
            }
        }
    }
    return ans
}
var shortestPalindrome = function(s) {
    let reverseS = s;
    reverseS = reverseS.split("").reverse().join("")
    let mergeS = s+" "+reverseS
    let KMPList = KMP(mergeS)

    return reverseS.slice(0,reverseS.length -KMPList[KMPList.length-1])+s;
    
};