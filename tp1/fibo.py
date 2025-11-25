from tp1.decorators import trace

#@trace
def fibo(n: int) -> int:
    if n==0:
        return 0
    elif n ==1:
        return 1
    else: return fibo(n-1)+fibo(n-2)

print(trace(fibo(6)))

def price(n):
    if n==0: return 0
    elif n==1: return 0
    else:
        return 1+price(n-1)+price(n-2)
print(price(10))

def fibo_norec(n):
    if( n == 0):
        return 0
    else:
        x = 0
        y = 1
        for i in range(1,n):
            z = (x + y)
            x = y
            y = z
    return y
print(fibo(10))
print(fibo_norec(10))

def fibo_term(n):
    def fibo_helper(n, a, b):
        if n == 0:
            return b
        else:
            return fibo_helper(n-1, a+b, a)
    return fibo_helper(n, 1, 0)

print(fibo_term(10))




