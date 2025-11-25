from stupidsort import is_sorted
def min(l:list[int]):
    m=l[0]
    for i in l:
        if i<m:
            m=i
    return m

def index(l:list[int],n):
    for i in range(len(l)):
        if i ==n:
            return i
def insertionsort(seq: list[int]) -> list[int]:
    n=len(seq)
    i=1
    j=i-1
    temp =seq[i]
    while j>=0 and seq[j]>temp:
        seq[j + 1] = seq[j]  # move bigger element right
        j -= 1
        seq[j + 1] = temp

def insertionsort(seq: list[int]) -> list[int]:
    n = len(seq)
    i = 1  # start from the second element
    while i < n:
        temp = seq[i]       # store the current key
        backofkey = i - 1           # start from the last element of the sorted portion
        # shift elements to the right until correct position for temp is found
        while backofkey >= 0 and seq[backofkey] > temp:
            seq[backofkey + 1] = seq[backofkey]
            backofkey -= 1
        seq[backofkey + 1] = temp   # insert the key in its correct position
        i += 1              # move to the next element
    return seq