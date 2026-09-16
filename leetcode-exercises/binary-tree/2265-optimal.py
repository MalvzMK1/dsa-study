class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.postOrder(root)
        return self.count

    def postOrder(self, root: TreeNode) -> tuple[int, int]:
        if root is None:
            return 0, 0
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        node_sum = left[0] + right[0] + root.val
        node_count = left[1] + right[1] + 1
        if node_sum // node_count == root.val:
            self.count += 1
        return (node_sum, node_count)

import time

print()

root = TreeNode(0, TreeNode(0), TreeNode(0))

start = time.perf_counter()
result = Solution().averageOfSubtree(root)
end = time.perf_counter()
elapsed_time = end - start
print(f"Result: {result}\nTook {elapsed_time:.6f}")

