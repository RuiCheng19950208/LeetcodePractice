#include<map>

class TrieNode{
public:
    int value;
    map<char,TrieNode*> nextChar;
    TrieNode(int v): value(v) {} 
    TrieNode(): value(0) {} 

};
class Solution {
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        TrieNode *root = new TrieNode();
        TrieNode *curNode = root;
        for(string word : words)
        {
            curNode = root;
            for(char c : word)
            {
                if (curNode->nextChar.find(c)==curNode->nextChar.end())
                {
                    curNode->nextChar[c] = new TrieNode();
                }
                curNode->nextChar[c]->value +=1;
                curNode = curNode->nextChar[c];
            }
            
        }

        vector<int> ans;
        int tempAns = 0;
        for(string word : words)
        {
            tempAns = 0;
            curNode = root;
            for(char c : word)
            {
                curNode = curNode->nextChar[c];
                tempAns += curNode->value;
            }
            ans.push_back(tempAns);
        }
        return ans;
    }
};