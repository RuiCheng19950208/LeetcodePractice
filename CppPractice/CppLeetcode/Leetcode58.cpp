class Solution {
public:
    int lengthOfLastWord(string s) 
    {
        istringstream iss(s);
        vector<string> words;
        string word;

        // Read words separated by spaces
        while (iss >> word) {
            words.push_back(word);
        }
        return words[words.size()-1].size();
    }
};