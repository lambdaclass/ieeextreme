#! /usr/bin/env python3

def query(guess):
    print('Q ' + ' '.join(guess))
    return int(input())

def answer(guess):
    print('A ' + ' '.join(guess))

n = int(input())

# Estado:
guess = ['0'] * n # Notar que '0' y '1' son strings
num_correctas = query(guess)

# Probamos bit por bit hasta encontrar la solución.
for i in range(n):
    guess[i] = '1'
    nuevo_num_correctas = query(guess)

    if nuevo_num_correctas == num_correctas + 1:
        num_correctas = nuevo_num_correctas
    else:
        # Damos marcha atrás.
        guess[i] = '0'

# ponemos la respuesta final.
answer(guess)
