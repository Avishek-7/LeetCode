# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        end = False

        while queue:
            current = queue.popleft()

            if current is None:
                end = True
            else:
                if end:
                    return False
                queue.append(current.left)
                queue.append(current.right)
        return True
        