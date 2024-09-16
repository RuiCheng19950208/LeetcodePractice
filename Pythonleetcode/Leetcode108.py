# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def to_bst(nums,start,end):
            if start>end:
                return None
            mid=(end+start)//2
            # print(mid)
            node=TreeNode(nums[mid])
            node.left=to_bst(nums,start,mid-1)
            node.right = to_bst(nums, mid+1, end)

            return node

        return to_bst(nums,0,len(nums)-1)

# print(Solution().sortedArrayToBST(nums = [-10,-3,0,5,9]))
