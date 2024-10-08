class TrieNode
{
    constructor(value = 0)
    {
        this.value = value;
        this.nextChar = {};
    }
}
var sumPrefixScores = function(words) {
    let root = new TrieNode();
    let curNode = root;
    for (let word of words) {
        curNode = root;
        for (let c of word) {
            if (curNode.nextChar.has(c)==false) {
                curNode.nextChar[c] = new TrieNode();

            }
            curNode.nextChar[c].value +=1;
            curNode = curNode.nextChar[c];
            
        }
    }
    let ans=[];
    let tempAns = 0;
    for (let word of words) {
        tempAns = 0;
        curNode = root;
        for (let c of word) {
            tempAns += curNode.nextChar[c].value ;
            curNode = curNode.nextChar[c];
            
        }
        ans.push(tempAns);
    }
    return ans;
};