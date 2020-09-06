#!/bin/python
# Inspirado en la respuesta de Ahmed Moussa

def print_solucion(solucion):
    if solucion:
        # Tenemos que devolver el mas chico primero
        print(min(solucion), max(solucion))
    else:
        print("!OK")

def buscar_solucion(S, L):
    sol = None

    buscados = set()
    for x in L:
        if x in buscados:
            sol = (x, S-x)
            break
        else:
            buscados.add(S-x)

    return sol

def bear_sums():
    S, _ = input().split() # S E
    S = int(S)

    L = [ int(s) for s in input().split() ]
    sol = buscar_solucion(S, L)
    print_solucion(sol)

T = int(input())
for _ in range(T):
    bear_sums()
