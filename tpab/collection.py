Point = tuple[float, float]
def distance_et_barycentre(A: Point, B: Point) -> tuple[float, Point]:
    xa=A[0]
    ya = A[1]
    xb = B[0]
    yb = B[1]

    dist=((xb-xa)**(2)+(yb-ya)**(2))**(1/2)
    cx=(xa+xb)/2
    cy=(ya+yb)/2
    center:Point=(cx,cy)
    return dist,center

print(distance_et_barycentre((3,4),(1,2)))

def dictsqrt():
    dico:dict[int,int]={}
    for i in range(100):
        dico[i]=i**2
    return dico

print(dictsqrt())

def consdico(a:list,b:list):
    dico:dict={}
    n=len(a)
    if n!=len(b): return 0
    for i in range(len(a)):
        dico[a[i]]=b[i]
    return dico

print(consdico([1,2,3,4,6],["a","b","c","c","o"]))

def moy(a:dict[str,int]):
    nb=0
    sum=0
    for i in a:
        if i=="error":
            pass
        else:
            nb+=1
            sum+=a[i]

    return sum/nb

print(moy({"aaa":4,"ccc":2,"error":10}))

def sorttt(d:dict):
    sorted_keys =  sorted(d, key= lambda x: d[x],reverse=True)
    return [d[k] for k in sorted_keys]

print(sorttt({"aaa":4,"ccc":2,"error":10}))

def dnk(seq:str):
    l=[]
    temp=""
    i, n = 0, 0
    while i < len(seq):
        if n<3:
            temp+=seq[i]
            n+=1
            i+=1
        else:
            l.append(temp)
            n=0
            temp=""
    return l

print(set(dnk("aucucggucgaccgcgcuuucaucgucggcaaagucaagaucccg")))

def compare(seq:str,seq2:str):
    dico:dict={}
    s1 = set(dnk(seq))
    s2 = set(dnk(seq2))
    total=s1|s2
    intersect=s1&s2
    diff=s1-s2
    return total,intersect,diff

print(compare("aucucggucgaccgcgcuuucaucgucggcaaagucaagaucccg","aucuuggucccuaggccuacg"))

def collect(s):
    l=[]
    countb=[(b,s.count(b))for b in set(s)]
    srt=sorted(countb, key=lambda x: x[1])
    return srt

print(collect("aucucggucgaccgcgcuuucaucgucggcaaagucaagaucccg"))