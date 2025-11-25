Tower = str
Move = (int, Tower, Tower)

def hanoi(n: int, org: Tower = 'A', dst: Tower = 'C', aux: Tower = 'B') -> list[Move]:
    if n==0:
        return []
    moves=[]
    moves += hanoi(n - 1, org, aux, dst)
    moves.append((n, org, dst))
    moves += hanoi(n - 1, aux, dst, org)
    return moves

print(hanoi(7))