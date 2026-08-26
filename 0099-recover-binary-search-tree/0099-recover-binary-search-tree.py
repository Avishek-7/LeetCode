# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = second = prev = None

        def find_swapped_nodes(node):
            nonlocal first, second, prev
            if not node:
                return 
            find_swapped_nodes(node.left)
            if prev and node.val < prev.val:
                if not first:
                    first = prev
                second = node
            prev = node
            find_swapped_nodes(node.right)
        
        find_swapped_nodes(root)
        if first and second:
            first.val, second.val = second.val, first.val
        