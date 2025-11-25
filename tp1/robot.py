from typing import List, Tuple
Board=List[Tuple]

def greedy_bot(damier: Board, l: int = 0, c: int = 0) -> int:
    gaintab = [[0 for _ in range(c)] for _ in range(l)]
    dict={}
    for (a,b,k) in damier:
        dict[(a,b)]=k
    filldict={}
    for i in range (l):
        for j in range (c):
            gain=dict.get((i,j),0)
            gain = dict.get((i, j), 0)
            up = gaintab[i - 1][j] if i > 0 else 0
            left = gaintab[i][j - 1] if j > 0 else 0
            gaintab[i][j] = gain + max(up, left)
    return gaintab[0][0]



print(greedy_bot([(0, 0, 9),(0, 1, 8),
                                (0, 2, 6),
                                (1, 0, 6),
                                (1, 1, 5),
                                (1, 2, 3)
                                ],2,3))
