# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        q1, q2 = collections.deque([t1]), collections.deque([t2])

        while q1 and q2:
            n1, n2 = q1.popleft(), q2.popleft()
            if n1 and n2:
                n1.val += n2.val

                if not n1.left and n2.left:
                    n1.left = TreeNode(0)
                if not n1.right and n2.right:
                    n1.right = TreeNode(0)

                q1.append(n1.left)
                q1.append(n1.right)
                q2.append(n2.left)
                q2.append(n2.right)

        return t1
