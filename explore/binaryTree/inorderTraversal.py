from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            result.extend(self.inorderTraversal(root.left))
            result.append(root.val)
            result.extend(self.inorderTraversal(root.right))
        return result

    def inorderTraversalIterativeSolution(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result


func = Solution()
print(func.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
print(func.inorderTraversalIterativeSolution(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
