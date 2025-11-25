def valabs(n:int)->int:
    if n<0:
        return -n
    else:
        return n

def isuneven(n:int)->bool:
    return n%2 != 0

def prodmod(n,p,m):
    return (n*p)%m

def divis(k,n) -> bool:
    return n/k

if __name__ == '__main__':
    prodmod(42, 7, 0)