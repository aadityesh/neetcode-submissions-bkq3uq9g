# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # if root is None: return

        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root
        if not root: return root

        from collections import deque
        q = deque()
        q.append(root)

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
                
        return root

        