def power(a: int, n: int) -> int:
    if n==0:
        return 1
    elif n==1:
        return a
    else:
        return power(a,n//2)*power(a,(n+1)//2)

#print(power(3,4))
#print(power(3,3))

def superpower(a,n):
    if n==0:
        return 1
    elif n==1:
        return a
    if n%2==0:
        return superpower(a,n//2)*superpower(a,n//2)
    else:
        return superpower(a,n//2)*superpower(a,n//2)*a

print(superpower(3,4))
#print(superpower(3,3))