#include<vector>
using namespace std;

class Solution {
private:
    void MoveToNext(int val)
    {   
        
        result[curPos.first][curPos.second]  =val;
        int nextRow = curPos.first + direction[directIndex].first;
        int nextCol =  curPos.second + direction[directIndex].second;
        if (nextRow<0||nextRow>publicm-1||nextCol<0||nextCol>publicn-1||result[nextRow][nextCol]!=-1)
        {
            directIndex = (directIndex+1)%4;
            nextRow = curPos.first + direction[directIndex].first;
            nextCol =  curPos.second + direction[directIndex].second;
        }

        curPos = make_pair(nextRow,nextCol);
    }

public:
    vector<vector<int>> result;
    vector<pair<int,int>> direction;
    int directIndex;
    pair<int,int> curPos;
    int publicm;
    int publicn;
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) 
    {
        result = vector<vector<int>>(m,vector<int>(n,-1));
        direction = {make_pair(0,1),make_pair(1,0),make_pair(0,-1),make_pair(-1,0)};
        directIndex = 0;
        curPos = make_pair(0,0);
        publicm=m;
        publicn=n;
        while (head)
        {
            MoveToNext(head.val);
            head = head->next;
        }
        return result;
    }
};