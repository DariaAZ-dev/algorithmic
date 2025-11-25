def sieve_of_eratosthenes(N: int) -> list[int]:
    l=[i for i in range(2,N+1)]
    newl=[]
    while l:
        temp=l.pop(0)
        l=[i for i in l if i%temp!=0]
        newl.append(temp)
    return newl

print(sieve_of_eratosthenes(11))