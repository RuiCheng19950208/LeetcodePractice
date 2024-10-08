class MyCalendarTwo {
public:
    vector<pair<int,int>> bookList;
    vector<pair<int,int>> doubleBookList;     
    MyCalendarTwo() {}
    bool book(int start, int end) {
        for(auto thePair:doubleBookList)
        {
            if (!(start>=thePair.second || end<=thePair.first))
            {
                return false;
            }
        }

        for(auto thePair:bookList)
        {
            pair<int,int> temp ;
            if (!(start>=thePair.second || end<=thePair.first))
            {
                temp = make_pair(max(thePair.first,start), min(thePair.second,end));
            }
            doubleBookList.push_back(temp);

        }
        bookList.push_back(make_pair(start, end));
        return true;
    }
};
