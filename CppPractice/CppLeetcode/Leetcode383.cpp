#inlcude<map>
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char,int> dictr;
        map<char,int> dictm;
        for(char c : ransomNote)
        {
            dictr[c]++;
        }
        for(char c : magazine)
        {
            dictm[c]++;
        }
        for(char c : ransomNote)
        {
            if (dictr[c]<dictm[c])
            {
                return false;
            }
        }
        return true;
    }
};