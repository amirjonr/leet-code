from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            result.extend(self.postOrderTraversal(root.left))
            result.extend(self.postOrderTraversal(root.right))
            result.append(root.val)
        return result

    def postorderTraversal(self, root):
        postOrder = []
        if not root:
            return postOrder

        stack = []
        cur = root
        lastVisited = None

        while cur or stack:
            if cur:
                stack.append(cur)
                print(f"Pushed Node: {cur.val}")  # Print the pushed value
                cur = cur.left
            else:
                temp = stack[-1]
                if temp.right and temp.right != lastVisited:
                    cur = temp.right
                    print(f"Moved to Right Child: {cur.val}")  # Print the moved value
                else:
                    stack.pop()
                    postOrder.append(temp.val)
                    print(f"Popped Node: {temp.val}")  # Print the popped value
                    lastVisited = temp

        return postOrder

    def postorderTraversalIterativeSolution(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.insert(-1, current.val)
            current = current.right
        return result


f = Solution()
print(f.postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
print(f.postorderTraversalIterativeSolution(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
