# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        ans = []

        def help(node):
            if not node:
                return
            help(node.left)
            ans.append(node.val)
            help(node.right)

        help(root)
        return ans

        """
        :type root: TreeNode
        :rtype: List[int]
        """