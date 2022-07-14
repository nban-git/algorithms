# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from idlelib.tree import TreeNode
from collections import defaultdict
from typing import Optional, List

from leetcode import TreeNode
from leetcode.Builder import buildTree, serialize, flattenNodes


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node: TreeNode) -> str:
            if not node:
                return "null"
            key = ','.join([str(node.val), traverse(node.left), traverse(node.right)])
            treeMap[key].append(node)
            return key

        treeMap = defaultdict(list)
        traverse(root)
        return [treeMap[key][0] for key in treeMap if len(treeMap[key]) > 1]


if __name__ == '__main__':
    sol = Solution()
    tree = buildTree([1, 2, 3, 4, None, 2, 4, None, None, 4])
    dupTrees = sol.findDuplicateSubtrees(tree)
    result = serialize(dupTrees)
    print(result)
    # == [[2, 4], [4]]

