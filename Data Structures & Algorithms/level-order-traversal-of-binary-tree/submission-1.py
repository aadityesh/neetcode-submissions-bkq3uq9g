# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root, ls, i):

        if not root: return
        if i == len(ls): ls.append([])
        ls[i].append(root.val)
        self.dfs(root.left, ls, i + 1)
        self.dfs(root.right, ls, i + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # if root == None:
        #     return []

        # q = deque()
        # q.append(root)

        # curr = root

        # level_order = []

        # while len(q) > 0:
            
        #     size = len(q)
        #     curr_level = []
            
        #     while size:
                
        #         front = q.popleft()

        #         if front.left:
        #             q.append(front.left)

        #         if front.right:
        #             q.append(front.right)
                
        #         curr_level.append(front.val)
                
        #         size -= 1
            
        #     level_order.append(curr_level)

        
        # return level_order

        ls = []
        self.dfs(root, ls, 0)
        return ls