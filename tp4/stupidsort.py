import random

def is_sorted(seq: list[int]) -> bool:
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

def fisher_yates(seq: list[int]) -> None:
    n = len(seq)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        seq[i], seq[j] = seq[j], seq[i]

def stupidsort(seq: list[int]) -> list[int]:
    """Bogosort: random shuffle until sorted."""
    while not is_sorted(seq):
        fisher_yates(seq)
    return seq

