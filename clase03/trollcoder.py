#! /usr/bin/env python3

def query(guess):
    print('Q ' + ' '.join(guess))
    return int(input())

def answer(guess):
    print('A ' + ' '.join(guess))

# ------------------------------------------------------------

# Estado:
n = int(input())
guess = ['0'] * n
num_correctas = query(guess) # 1 intento

for i in range(n): # N intentos
    guess[i] = '1'
    nuevo_num_correctas = query(guess)

    if nuevo_num_correctas == num_correctas + 1:
        num_correctas = nuevo_num_correctas
    else:
        guess[i] = '0'

# N + 1 intentos
answer(guess)
