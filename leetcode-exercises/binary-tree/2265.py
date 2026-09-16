class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = {'el_count': 0}
        self.dfs(root, result)
        return result['el_count']

    def dfs(self, root: TreeNode, result: dict[str, int]) -> None:
        sub_sum, sub_el = self.process_subtree(root)
        if sub_sum // sub_el == root.val:
            result['el_count'] += 1
        if root.left is not None:
            self.dfs(root.left, result)
        if root.right is not None:
            self.dfs(root.right, result)

    def process_subtree(self, root: TreeNode, sum_result: int = 0) -> tuple[int, int]:
        sum_result += root.val
        elements = 1
        if root.left is not None:
            s, e = self.process_subtree(root.left)
            sum_result += s
            elements += e
        if root.right is not None:
            s, e = self.process_subtree(root.right)
            sum_result += s
            elements += e
        return sum_result, elements


import time

print()

root = TreeNode(0, TreeNode(0), TreeNode(0))

start = time.perf_counter()
result = Solution().averageOfSubtree(root)
end = time.perf_counter()
elapsed_time = end - start
print(f"Result: {result}\nTook {elapsed_time:.6f}")

