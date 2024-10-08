class MyCalendar {
public:
    vector<pair<int,int>> bookList;
    MyCalendar() {}
    bool book(int start, int end) {
        for(auto pair:bookList)
        {
            if(start<pair.second && end>pair.first){return false;}
        }
        bookList.push_back(make_pair(start,end));
        return true;
    }
};
