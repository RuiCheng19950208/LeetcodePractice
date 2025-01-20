
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;
    
    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}

public class Solution138 {
    public Node CopyRandomList(Node head) 
    {
        if(head==null){return null;}
        Dictionary<Node,Node> theMap = new Dictionary<Node,Node>();
        Node cur = head;
        while(cur!=null)
        {
            theMap[cur] = new Node(cur.val);
            cur=cur.next;
        }
        cur=head;
        while(cur!=null)
        {
            if(cur.next!=null){theMap[cur].next = theMap[cur.next];}
            if(cur.random!=null){theMap[cur].random = theMap[cur.random];}
            cur=cur.next;
        }
        return theMap[head];
        
    }
}