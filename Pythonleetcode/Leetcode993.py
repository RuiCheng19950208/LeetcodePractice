class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def check_value(target,target_depth,val,depth):
            if val==target[0]:
                target_depth[0]=depth
            elif val==target[1]:
                target_depth[1] = depth
            return target_depth


        if not root:
            return False
        target=[x,y]
        temp=[[root,0]]
        target_depth=[-1,-2]
        while len(temp)>0:
            a=temp.pop()
            if a[0].left and a[0].right:
                if a[0].left.val in target and a[0].right.val in target:
                    return False
                else:
                    target_depth = check_value(target, target_depth, a[0].left.val , a[1]+1)
                    target_depth = check_value(target, target_depth, a[0].right.val, a[1] + 1)
                    if target_depth[0]==target_depth[1]:
                        return True
                temp.append([a[0].left , a[1] + 1])
                temp.append([a[0].right, a[1] + 1])
            elif a[0].left:
                target_depth = check_value(target, target_depth, a[0].left.val, a[1] + 1)
                if target_depth[0] == target_depth[1]:
                    return True
                temp.append([a[0].left, a[1] + 1])

            elif a[0].right:
                target_depth = check_value(target, target_depth, a[0].right.val, a[1] + 1)
                if target_depth[0] == target_depth[1]:
                    return True
                temp.append([a[0].right, a[1] + 1])

        return False


