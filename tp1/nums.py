def count_digits(n: int, base: int) -> int:
    if n < base:
        return 1
    return 1 + count_digits(n // base, base)

print(count_digits(4_567_890,10))
print(count_digits(4_002_110,2))
print(count_digits(4398046511104, 3))
def convert(n: int, base: int) -> str:
    l=[]
    c=0
    while n!=0:
        l.append(n%base)
        n=n//base
    l.reverse()
    for i in l:
        c=c*10+i
    return str(c)
print(convert(10,2))
print(convert(2555,9))