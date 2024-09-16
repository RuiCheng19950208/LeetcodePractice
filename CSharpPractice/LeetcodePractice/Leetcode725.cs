public class Solution725 {
    public ListNode[] SplitListToParts(ListNode head, int k) {
        ListNode cur = head;
        int listLen = 0;
        while (cur!=null)
        {
            cur =cur.next;
            listLen++;
        }
        int averageLen = listLen/k;
        int remainder = listLen%k;
        ListNode[] ans = new ListNode[k];
        cur = head;
        for (var i = 0; i < k; i++)
        {
            ListNode partHead = cur;
            int partLen = averageLen+(i<remainder?1:0);
            for (int j = 0; j < partLen-1; j++)
            {
                cur = cur.next;
            }
            if (cur!=null)
            {
                ListNode nextHead = cur.next;
                cur.next = null;
                cur = nextHead;
            }
            ans[i] = partHead;
        }
        return ans;
    }
}