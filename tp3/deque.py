from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Iterator
from tp5.btree import *
from tp3.linkedlist import (LinkedList,
                        ll_new,
                        ll_is_empty,
                        ll_len,
                        ll_str,
                        ll_head,
                        ll_tail,
                        ll_prepend,
                        ll_append,
                        ll_remove)


@dataclass
class Deque:
    ll: LinkedList


def d_new() -> Deque:
    return Deque(ll_new())


def d_is_empty(d: Deque) -> bool:
    return ll_is_empty(d.ll)


def d_len(d: Deque) -> int:
    return ll_len(d.ll)


def d_str(d: Deque) -> str:
    return ll_str(d.ll)


def d_front(d: Deque) -> int:
    if ll_is_empty(d.ll):
        raise IndexError('Unable to get front of an empty deque')
    return ll_head(d.ll).item


def d_rear(d: Deque) -> int:
    if ll_is_empty(d.ll):
        raise IndexError('Unable to get rear of an empty deque')
    return ll_tail(d.ll).item


def d_push_front(d: Deque, item: int) -> Deque:
    ll_prepend(d.ll, item)
    return d
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


def d_push_rear(d: Deque, item: int|Node) -> Deque:
    ll_append(d.ll, item)
    return d


def d_pop_front(d: Deque) -> Deque:
    if ll_is_empty(d.ll):
        raise IndexError('Unable to pop the front of an empty deque')
    ll_remove(d.ll, ll_head(d.ll))
    d.ll.scrit.sled=ll_head(d.ll)
    return d

def d_pop_rear(d: Deque) -> Deque:
    if ll_is_empty(d.ll):
        raise IndexError('Unable to pop the rear of an empty deque')
    ll_remove(d.ll, ll_tail(d.ll))
    d.ll.scrit.sled = ll_tail(d.ll)
    return d