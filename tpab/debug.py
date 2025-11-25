numbers: list[int] = list(range(10))

n=len(numbers)
i=0

while i<n:
    if numbers[i] % 2 ==0:
        del numbers[i]
        n-=1
    else:
        numbers[i] *= i
        i+=1
print(numbers)
