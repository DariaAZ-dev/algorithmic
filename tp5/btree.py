from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Iterator
from tp3.deque import *


@dataclass
class BinaryTree:
    """
    A binary tree is a tree data structure in which each node has at most two children,
    which are referred to as the left child and the right child.

    The BinaryTree class is a dataclass with a single field, root, which is a reference to the root node of the tree.

    The Node class is a nested dataclass with three fields: key, left, and right.
    The key field is an integer that stores the value of the node.
    The left and right fields are references to the left and right children of the node, respectively.

    Example:
        >>> bt = BinaryTree(Node(2, Node(1, Node(0)), Node(4, Node(3), Node(5))))
    """
    root: Node | None = None


@dataclass
class Node:
    key: int
    left: Node | None = None       # "Or None" for terminal nodes
    right: Node | None = None



def bt_is_empty(bt: BinaryTree) -> bool:
    return bt.root.key is None


def bt_root(bt: BinaryTree) -> Node:
    return bt.root


def bt_iter_dfs(n: Node) -> Iterator[Node]:
    if n is not None:
        # alt. yield from bt_iter_dfs(n.left)
        for ng in bt_iter_dfs(n.left):
            yield ng
        yield n
        for nd in bt_iter_dfs(n.right):
            yield nd

def dpered(d: Deque) ->Node:
    if ll_is_empty(d.ll):
        raise IndexError('Unable to get front of an empty deque')
    return ll_head(d.ll).item

def bt_iter_bfs(n: Node) -> Iterator[Node]:
    l=d_new()
    if n is not None and n.key is not None:
        d_push_rear(l,n)
        while not d_is_empty(l):
            nd=dpered(l)
            d_pop_front(l)
            yield nd
            if nd.left is not None:
                d_push_rear(l, nd.left)
            if nd.right is not None:
                d_push_rear(l, nd.right)






def bt_height(bt: BinaryTree) -> int:
    def height(node) -> int:
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))

    return height(bt.root)


def bt_size(bt: BinaryTree) -> int:
    def size(node) -> int:
        if node is None:
            return 0
        return 1 + size(node.left) + size(node.right)

    return size(bt.root)


def bt_str(bt: BinaryTree) -> str:
    if bt is None:
        return "()"
    left_str = bt_str(bt.left)
    right_str = bt_str(bt.right)
    return f"{bt.key} {left_str} {right_str}" if bt.left or bt.right else f"{bt.key}"

def bt_new(nodes: list[int | None] | None = None) -> BinaryTree:
    if not nodes or all(n is None for n in nodes):
        return None

    def build(i: int):
        if i >= len(nodes) or nodes[i] is None:
            return None
        left = build(2 * i + 1)
        right = build(2 * i + 2)
        return Node(nodes[i], left, right)

    return build(0)


def bt_is_bst(bt: BinaryTree) -> bool:
    raise NotImplementedError("bt_is_bst function not implemented yet")


def bt_is_heap(bt: BinaryTree) -> bool:
    raise NotImplementedError("bt_is_heap function not implemented yet")


def bt_lca(bt: BinaryTree, a: int, b: int) -> int:
    raise NotImplementedError("bt_lca function not implemented yet")


def bt_prettystr(bt: BinaryTree) -> str:
    raise NotImplementedError("bt_prettystr function not implemented yet")


if __name__ == '__main__':
    a = BinaryTree(Node(0, Node(1, Node(3), Node(4)), Node(2, Node(5), Node(6))))