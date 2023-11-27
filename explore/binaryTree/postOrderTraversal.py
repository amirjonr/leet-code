from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is not None:
            result.extend(self.postOrderTraversal(root.left))
            result.extend(self.postOrderTraversal(root.right))
            result.append(root.val)
        return result
    def postorderTraversalIterativeSolution(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        while root or stack:
            while root.left:
                result.append(root.left)
                stack.append(root)
            root = stack.pop(root.left)
            root = root.val

        return result


f = Solution()
print(f.postOrderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
print(f.postorderTraversalIterativeSolution(TreeNode(1, None, TreeNode(2, TreeNode(3)))))

# TODO all this solutions is trivial, try to solve iteratively