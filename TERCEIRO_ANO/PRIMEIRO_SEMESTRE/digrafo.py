import numpy as np


def ShowDigrafo():
    
    entry = input("Arestas do Digrafo: (origem, destino, origem destino, ...)")
    edges = np.array([[int(v) for v in ar.split(" ") if v.strip()] for ar in entry.split(',') if ar.strip()])
    
    # print(edges[0][0])
    # print(max)

    #================== PEGADO MAIOR DESTINO =======================#

    destiny = []
    for v in edges:
        destiny.append(v[1])
        
    destiny = np.array(destiny)
    d_max   = destiny.max()

    #===============================================================#

    #================== PEGADO MAIOR ORIGEM =======================#

    origin = []
    for v in edges:
        origin.append(v[0])
        
    origin = np.array(origin)
    o_max   = origin.max()

    #===============================================================#
   
    #================== IMPRIMINDO CABEÇALHO =======================#

    cont = 1
    print(f"V | ", end="")
    for d in range(d_max):  # Pensar se sempre vai começar do 1 ou nn
        print(cont, end=" ") if d < d_max - 1 else print(cont)
        cont += 1

    print("---"*d_max)

    #===============================================================#

    #==================  ESPELHANDO DIGRAFO  =======================#
    
    # mirror = [[["0"]] * d_max] * o_max
    mirror = [["0" for _ in range(d_max)] for _ in range(o_max)]

    for v in edges:
        mirror[(v[0]-1)][(v[1]-1)] = "1"
        # print(v[0])
        # print(v[1])

    #================== IMPRIMINDO AS LINHAS =======================#
    cont = 1

    
    for line in mirror:
        print(cont, "| ", end="")

        for col in line:
            print(col,f"", end="")

        print(f"\n", end="")

        cont += 1


    
    # print(mirror)
ShowDigrafo()

