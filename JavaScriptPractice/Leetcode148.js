var sortList = function(head) {
    let cur = head;
    let numList = [];
    while(cur!=null)
    {
        numList.push(cur.val);
        cur=cur.next;
    }
    cur=head;
    let index =0;
    numList.sort((a,b)=>a-b);
    while(cur!=null)
    {
       cur.val  = numList[index];
       index++;
       cur=cur.next;
    }
    return head;
};