class Solution {
public:
    bool isCircularSentence(string sentence) 
    {
        stringstream ss(sentence);
        vector<string> sList;
        string word;
        while(ss>>word)
        {
            sList.push_back(word);
        }
        int n =  sList.size();
        for(int i=0;i<n-1;i++)
        {
            if(sList[i][sList[i].size()-1]!=sList[i+1][0])
            {
                return false;
            }
        }
        if(sList[n-1][sList[n-1].size()-1]!=sList[0][0])
        {
            return false;
        }
        return true;
    }
};