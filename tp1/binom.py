

def binom(n: int, k: int) -> int:
    if k==0 or k==n:
        return 1
    else:
        return binom(n-1,k-1)+binom(n-1,k)

print(binom(5,3))
print(binom(10,5))
print(binom(42,1))
#print(binom(100,50))

def binom_memo(n,k,memo):
    if memo is None:
        memo = {}
    if (n, k) in memo:
        return memo[(n, k)]
    if k == 0 or k == n:
        memo[(n, k)] = 1
    else:
        memo[(n, k)] = binom_memo(n - 1, k - 1, memo) + binom_memo(n - 1, k, memo)
    return memo[(n, k)]

print(binom_memo(5,3,{}))
print(binom_memo(100,50,{}))