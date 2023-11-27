from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversalRecursiveSolution(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is not None:
            result.append(root.val)
            result.extend(self.preorderTraversalRecursiveSolution(root.left))
            result.extend(self.preorderTraversalRecursiveSolution(root.right))
        return result
    def preorderTraversalIterativeSolution(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        while stack or root:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return result


func = Solution()
print(func.preorderTraversalRecursiveSolution(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
print(func.preorderTraversalIterativeSolution(TreeNode(1, None, TreeNode(2, TreeNode(3)))))