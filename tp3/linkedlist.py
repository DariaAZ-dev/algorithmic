# content of tp3/linkedlist.py
from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Iterator
from typing import Any



@dataclass
class LinkedList:
    scrit:Cell
    dlina:int


@dataclass(eq=False)
class Cell:
    item: int
    sled:Cell
    pred:Cell


def ll_new2(initial_l: list[int] | None = None) -> LinkedList:
    c=Cell(None,None,None)
    c.sled = c
    c.pred=c
    l=LinkedList(c,0)
    return l

def ll_is_empty(l: LinkedList) -> bool:
    return l.dlina==0


def ll_head(l: LinkedList) -> Cell:
    return l.scrit.sled


def ll_tail(l: LinkedList) -> Cell:
    return l.scrit.pred


def ll_append(l: LinkedList, item: int) -> Cell:
    l.dlina+=1
    new=Cell(item, l.scrit, l.scrit.pred)
    (l.scrit.pred).sled=new
    l.scrit.pred=new
    return new

def ll_new(initial_l: list[int] | None = None) -> LinkedList:
    initial_l = initial_l if initial_l is not None else []
    newl=ll_new2()
    for i in initial_l:
        ll_append(newl,i)
    return newl

def ll_iter(l: LinkedList, reverse: bool=False) -> Iterator[Cell]:
    current = ll_head(l)
    if not ll_is_empty(l):
        if not reverse:# vérifie que la liste n'est pas vide
            current= ll_head(l)
        else: current=ll_tail(l)# initialise la variable current à la tête de liste
    if reverse:
        while current is not l.scrit:
            yield current
            current = current.pred  # Move to the previous node
    else:
        while current is not l.scrit:
            yield current
            current = current.sled  # Move to the next node


def ll_len(l: LinkedList) -> int:
    return l.dlina


def ll_str(l: LinkedList) -> str:
    s="["
    el=(l.scrit).sled
    if l.dlina==0:
        return "[]"
    while el.sled != l.scrit:
        s=s+str(el.item)+", "
        el=el.sled
    s=s+str(el.item)+"]"
    return s

def ll_lookup(l: LinkedList, item: int) -> Cell|None:
    for c in ll_iter(l):
        if c.item==item:
            return c
    return None


def ll_cell_at(l: LinkedList, i: int) -> Cell:
    val=ll_lookup(l,i)
    if val is None:
        raise IndexError("LinkedList dos not contian it")
    else:
        return val

def ll_prepend(l: LinkedList, item: int) -> Cell:
    new = Cell(item, l.scrit.sled, l.scrit)
    l.dlina+=1
    l.scrit.sled=new
    return new

def ll_insert(l: LinkedList, item: int, next_to: Cell) -> Cell:
    for c in ll_iter(l):
        if c==next_to:
            l.dlina+=1
            new = Cell(item, c.sled, c)
            c.sled=new
            return new
    raise IndexError("LinkedList dos not contian it")

def ll_remove(l: LinkedList, cell: Cell) -> int:
    for c in ll_iter(l):
        if c==cell:
            l.dlina-=1
            pr=c.pred
            sl=c.sled
            pr.sled=sl
            sl.pred=pr
            return c.item
    return -1

def ll_extend(l1: LinkedList, l2: LinkedList) -> None:
    raise NotImplementedError("LinkedList ll_extend function not yet implemented")
