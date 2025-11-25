def collatz_lifetime(seed):
    return 42

def collatz_series(seed, index):
    return [1,2,3]

def collatz_altitude(seed):
    return 1


if __name__ == '__main__':
    a = collatz_lifetime(12)
    b = collatz_series(1,2)
    c = collatz_altitude(1)

    print(a, b, c)
