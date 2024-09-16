
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root==None:
            return
        temp=[root]
        ans=[]
        while len(temp)>0:
            a=temp.pop()
            ans.insert(0,a.val)
            for child in a.children:
                if child:
                    temp.append(child)


        return ans


