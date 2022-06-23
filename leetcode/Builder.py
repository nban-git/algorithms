from typing import List

from DataTypes import TreeNode
from queue import Queue


def buildTree(input: List[int]) -> TreeNode:
    if len(input) == 0:
        return None

    root = TreeNode(input[0])
    q = Queue()
    q.put(root)

    i = 1
    while not q.empty():
        cur = q.get()
        if i < len(input):
            if input[i] is not None:
                newNode = TreeNode(input[i])
                cur.left = newNode
                q.put(newNode)
            i += 1
        if i < len(input):
            if input[i] is not None:
                newNode = TreeNode(input[i])
                cur.right = newNode
                q.put(newNode)
            i += 1

    return root


def serialize(nodeList: TreeNode) -> List[int]:
    def bfs(node: TreeNode, nodes: List[int]):
        if node is None:
            return
        nodes.append(node.val)
        bfs(node.left, nodes)
        bfs(node.right, nodes)

    result = []
    for node in nodeList:
        nodes = []
        bfs(node, nodes)
        result.append(nodes)
    return result


def flattenNodes(nodes: List[TreeNode]) -> List[int]:
    result = []
    for node in nodes:
        result.append(node.val)
    return result
