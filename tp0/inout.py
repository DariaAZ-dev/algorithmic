def input_number_from_kb(prompt: str='Saisir un nombre entier : ') -> int:
    print(prompt)
    a = input()
    try:
        return int(a)
    except ValueError:
        print("write a real number")
        return input_number_from_kb(prompt)


import sys, argparse
def input_nums_from_cli() -> list[int]:
    l=[]
    a=[]
    c=0
    for j in sys.argv[1:]:
        a.append(j)
    if a[0] == '--sum':
        for i in a[1:]:
            try:
                c=c+int(i)
            except ValueError:
                print("write a real number")
                quit()
        l.append(c)
    elif a[0] == '--help':
        print("usage: python -m tp0.inout [--help] [--sum] [NOMBRE ...]\nCollecte les nombres passés en ligne de commande\narguments:\nNOMBRE série de nombres à collecter\noptions:\n--help affiche ce message d'aide et termine\n--sum réalise la somme des nombres")
    elif a[0] == "--file":
        data: str
        with open(a[1], 'r') as input_file:
            data = input_file.read()
            newl = data.split("\n")
            for i in newl:
                if i != "":
                    l.append(int(i))
    else:
        for i in a:
            try:
                l.append(int(i))
            except ValueError:
                print("write a real number")
                quit()
    return l




if __name__ == '__main__':
    #print(input_number_from_kb('Saisir un nombre entier : '))
    print(input_nums_from_cli())
    #print("[",end="")
    #for i in sys.argv[1:-1]: print(f"{i}, ",end="")
    #print(f"{sys.argv[-1]}", end="")
    #print("]")