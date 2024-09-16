
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        ans=0
        pair_list=[[root,1]]
        while len(pair_list)>0:
            a=pair_list.pop()
            if ans<a[1]:
                ans=a[1]
            for child in a[0].children:
                if child:
                    pair_list.append([child,a[1]+1])
        return ans


