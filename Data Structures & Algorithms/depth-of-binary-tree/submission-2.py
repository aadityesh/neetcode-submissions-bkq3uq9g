# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # if root is None: return 0

        # lh = self.maxDepth(root.left)
        # rh = self.maxDepth(root.right)

        # return max(lh, rh) + 1

        if not root: return 0
        
        from collections import deque
        q = deque()
        q.append(root)
        level = 0

        while q:
            
            size = len(q)
            
            while size:

                front = q.popleft()

                if  front.left: 
                    q.append(front.left)

                if  front.right: 
                    q.append(front.right)

                front.left, front.right = front.right or None, front.left or None
                
                size -= 1

            level += 1

                
        return level
        