var copyRandomList = function(head) 
{
    let cur = head;
    let theMap = new Map();
    while(cur)
    {
        theMap.set(cur,new Node(cur.val));
        cur = cur.next;
    }
    cur=head;
    while(cur)
    {
        if(cur.next){theMap.get(cur).next = theMap.get(cur.next);}
        if(cur.random){theMap.get(cur).random = theMap.get(cur.random);}
        cur = cur.next;
    }
    return theMap.get(head);
};