data: str
with open('/home/ETUDIANT/e25c970e/tp_algo/tp0/data/online_inventaire_prevert.txt', 'r') as input_file:
    data = input_file.read()
    newdata=data.split(";")

with open('/home/ETUDIANT/e25c970e/tp_algo/tp0/data/inventaire_prevert.txt', 'w') as output_file:
    c=0
    for i in newdata:
        if i!="":
            output_file.write(f"{c:02d} {i}\n")
            c+=1