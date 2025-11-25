# content of tp2/arraylist.py
from dataclasses import dataclass
from tp2.util import StaticArray, alloc

@dataclass
class ArrayList:
    max_size:int
    lis: StaticArray
    size: int

def al_new(m: int = 10, l: list[int] | None = None) -> ArrayList:
    l = l if l is not None else []

    assert m >= len(l), "taille de liste trop grande"
    new_l = alloc(m)

    for i in range(len(l)):
       new_l[i] = l[i]

    return ArrayList(m, new_l, len(l))


tab = al_new(1000, [1,4,3,5])

def al_len(tab: ArrayList) -> int:
    return tab.size

def al_is_empty(tab: ArrayList) -> bool:
    return tab.size==0

def al_str(tab: ArrayList) -> str:
    s="["
    i=0
    if tab.size>0:
        while i < (tab.size-1):
            s+=f"{tab.lis[i]}, "
            i+=1
        s+=f"{tab.lis[i]}"
    else:
        pass
    s+="]"
    return s

def al_get(tab: ArrayList, i: int) -> int:
    if i >= tab.size or i < 0:
        raise IndexError(f"Index {i} out of bounds")
    return tab.lis[i]

def al_set(tab: ArrayList, i: int, item: int) -> ArrayList:
    if i >= tab.size or i < 0 or (item is None):
        raise IndexError(f"Index {i} out of bounds")
    tab.lis[i]=item
    return tab

def al_lookup(tab: ArrayList, item: int) -> int | None:
    for i in range(tab.size-1):
        if tab.lis[i]==item:
            return i
    return None

def al_remove(tab: ArrayList, i: int) -> ArrayList:
    if i >= tab.size or i < 0:
        raise IndexError(f"Index {i} out of bounds")
    temp=tab.lis[i]
    while i<tab.size:
        temp = tab.lis[i]
        tab.lis[i]=tab.lis[i+1]
        i+=1
    tab.lis[i]=None
    tab.size-=1
    return tab

def al_insert(tab: ArrayList, i: int, item: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_insert function not implemented yet")


def al_prepend(tab: ArrayList, item: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_prepend function not implemented yet")


def al_append(tab: ArrayList, item: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_append function not implemented yet")


def al_extend(tab1: ArrayList, tab2: ArrayList) -> ArrayList:
    raise NotImplementedError("ArrayList al_extend function not implemented yet")


