from util import StaticArray, alloc
def mode(tab: StaticArray) -> int:
    dico={}
    maxi=0
    for i in tab:
        for j in tab:
            if j==i:
                maxi+=1
        dico[i]=maxi
    m=0
    temp =-1
    for k in dico:
        if dico[k]>m:
            m=dico[k]
            temp=k
    return temp

def cumulative_sum(tab: StaticArray) -> StaticArray:
    s=0
    l=[]
    for i in tab:
        s+=i
        l.append(s)
    return l




if __name__ == '__main__':
    # comprehensive example
    tab: StaticArray = alloc(5)  # allocate a new fresh array of 5 contiguous integers
    print(tab)  # print [0, 0, 0, 0, 0] on stdout
    tab[2] = 2  # write the third value => [0, 0, 2, 0, 0]
    for i in range(len(tab)):  # loop over the indexes of the array, from 0 to the length - 1
        print(i, tab[i])  # => 0 0\\ 1 0\\ 2 2\\ 3 0\\ 4 0
    print(nops(tab))  # => {'nread': 5, 'nwrite': 1}
    reset_nops(tab)  # reset read/write counts
    print(tab, nops(tab))  # => [0, 0, 2, 0, 0] {'nread': 0, 'nwrite': 0}
    # for e in tab: print(e)                   # TypeError: 'StaticArray' object is not iterable
    # x = tab[1:3]                             # ValueError: Index slice(1, 3, None) must be an integer
    tab2 = random_array(10, 0, 2, True)  # create a sorted array of 10 random integers
    print(f"{tab2=!s}")  # print on stdout (values between 0 and 2)
    print(f"{nops(tab2)=}")