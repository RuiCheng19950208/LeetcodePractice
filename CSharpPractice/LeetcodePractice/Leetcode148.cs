public class Solution148 {
    public ListNode SortList(ListNode head) {
        List<int> numList = new List<int>();
        ListNode cur = head;
        while(cur!=null)
        {
            numList.Add(cur.val);
            cur = cur.next;
        }
        numList.Sort();
        cur = head;
        int curIndex=0;
        while(cur!=null)
        {
            cur.val  = numList[curIndex];
            curIndex++;
            cur=cur.next;
        }
        return head;
    }
}