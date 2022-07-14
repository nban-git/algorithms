from collections import defaultdict
from typing import Optional, List

from leetcode import TreeNode
from leetcode.Builder import buildTree


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        # at least 6 characters, at most 20
        # at least one lowercase, at least one uppercase, at least on digit
        # no three repeating characters in a row
        n = len(password)
        if n < 6:
            return 6 - n
        if n > 20:
            return n - 20

        lower, upper, digit, three, repeat = 0, 0, 0, 0, 1
        dict = {}
        for i in range(n):
            if password[i].isnumeric():
                digit = 1
            elif password[i].islower():
                lower = 1
            else:
                upper = 1
            if i == 0 or password[i] != password[i-1]:
                dict[password[i]] = 1
            else:
                dict[password[i]] += 1

        replace = 0
        if lower == 0: replace += 1
        if upper == 0: replace += 1
        if digit == 0: replace += 1

        repeats = 0
        for key in dict:
            if dict[key] >= 3:
                repeats += (dict[key] // 2)
                if replace > 0:
                    replace -= 1

        return max(replace, repeats)

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # inorder parsing
        def dfs(node: TreeNode, parent: TreeNode):
            if not node:
                return 0, 0
            linc, ldec = dfs(node.left, node)
            rinc, rdec = dfs(node.right, node)
            nonlocal longest
            longest = max(longest, linc + rdec +1, ldec + rinc + 1)
            if node.val == parent.val + 1:
                return max(linc, rinc) + 1, 0
            if node.val == parent.val - 1:
                return 0, max(ldec, rdec) + 1
            return 0, 0
        longest = 0
        dfs(root, root)
        return longest

    def longestConsecutiveSeq(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, parent: TreeNode):
            if not node:
                return 0
            left = dfs(node.left, node)
            right = dfs(node.right, node)
            nonlocal longest
            longest = max(longest, max(left, right) + 1)
            if node.val == parent.val + 1:
                return max(left, right) + 1
            return 0
        longest = 0
        dfs(root, root)
        return longest

    # 1 <= n <= 1000
    # edges.length == n - 1
    # edges[i].length == 2
    # 0 <= node1i, node2i <= n - 1
    # node1i != node2i
    # 1 <= query.length <= 1000
    # query[i].length == 3
    # 0 <= starti, endi, nodei <= n - 1
    # TODO work on this
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Tree, DFS, BFS
        def findpath(v, w, graph):
            stack = [v]
            visited = set()
            result = []
            while stack:
                next = stack.pop()
                result.append(next)
                if next == w:
                    return result
                visited.add(next)
                for x in graph[next]:
                    if x not in visited:
                        stack.append(x)

        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        for v, w, x in query:
            findpath(v, w)

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            next = self.inorderSuccessor(root.left, p)
            return



def Q420():
    sol = Solution()
    assert sol.strongPasswordChecker("a") == 5
    assert sol.strongPasswordChecker("aA1") == 3
    assert sol.strongPasswordChecker("1337C0d3") == 0
    assert sol.strongPasswordChecker("aaa123") == 1
    assert sol.strongPasswordChecker("aaa123BBB") == 2
    assert sol.strongPasswordChecker("aaa123bb") == 1
    # assert sol.strongPasswordChecker("1111111111") == 3
    assert sol.strongPasswordChecker("aaa111") == 2
    assert sol.strongPasswordChecker("11111111111111111111") == 6

def Q549():
    #  DFS, Binary Tree, Tree
    # Similar question 298, 128

    sol = Solution()
    # assert sol.longestConsecutive(buildTree([1,2,3])) == 2
    # assert sol.longestConsecutive(buildTree([2,1,3])) == 3
    # assert sol.longestConsecutive(buildTree([2,1,3,None,None,4,5])) == 4

    assert sol.longestConsecutiveSeq(buildTree([1,None,3,2,4,None,None,None,5])) == 3
    assert sol.longestConsecutiveSeq(buildTree([2,None,3,2,None,1])) == 2
    assert sol.longestConsecutiveSeq(buildTree([3,None,4,5,None,6])) == 4

def Q2277():
    sol = Solution()
    assert sol.closestNode(n = 7, edges = [[0,1],[0,2],[0,3],[1,4],[2,5],[2,6]], query = [[5,3,4],[5,3,6]]) == [0, 2]
    assert sol.closestNode(n = 3, edges = [[0,1],[1,2]], query = [[0,1,2]]) == [1]
    assert sol.closestNode(n = 3, edges = [[0,1],[1,2]], query = [[0,0,0]]) == [0]


if __name__ == '__main__':
    # Q420()
    Q549()
