class Solution {
public:
    bool isPalindrome(string s) {
        string newString="";
        for(char c:s)
        {
            if(c>='A'&&c<='Z'){c=c-'A'+'a';newString+=c;}
            else if((c>='a'&&c<='z')||(c>='0'&&c<='9')){newString+=c;}
        }
        for(int i=0;i<newString.size()/2;i++)
        {
            if(newString[i]!=newString[newString.size()-1-i]){return false;}

        }
        return true;
    }
};