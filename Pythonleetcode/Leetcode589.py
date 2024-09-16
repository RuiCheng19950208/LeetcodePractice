# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution(object):
    def preorder(self, root):
        if not root:
            return
        ans=[]
        temp=[root]
        while len(temp)>0:
            a=temp.pop()
            ans.append(a.val)
            for child in a.children[::-1]:
                if child:
                    temp.append(child)
        return ans