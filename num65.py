from typing import List


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):

      return f"TreeNode со значением {self.val}"


def traverse_in_order(root: TreeNode) -> List[int]:  # Итеративный обход
    """
    Обход двоичного дерева, возвращается список значений по порядку
    """
    answer = []
    stack = [(root, False)]   # (узел, посещен ли он еще)

    while stack:
        node, visited = stack.pop()

        if node:

            if visited:
                answer.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))

    return answer


if __name__ == '__main__':
    # Уровень 0
    root = TreeNode('a')

    # Уровень 1
    root.left = TreeNode('b')
    root.right = TreeNode('c')

    # Уровень 2
    root.left.left = TreeNode('d')
    root.left.right = TreeNode('e')

    root.right.left = TreeNode('f')
    root.right.right = TreeNode('g')

    #            a
    #          /   \
    #         b     c
    #        / \   / \
    #       d   e f   g