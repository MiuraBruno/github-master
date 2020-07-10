from concurrent.futures import *
from functools import reduce
from math import floor
from math import sqrt
from time import time


def primo(n):
    if n % 2 == 0: return n == 2
    divisor = 3
    raiz = floor(sqrt(n))
    while divisor <= raiz and n % divisor != 0:
        divisor += 2
    return n > 1 and divisor > raiz

def fatorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

def tri(n):
    return reduce(lambda x,y: x+y, range(1,n+1))



def main():
    number = [91781,45182,32345,17823,12313,62314,864352]
    start = time()
    results = list(map(primo, number))
    results = list(map(fatorial,number))
    results = list(map(tri,number))
    end = time()
    print('teste serial')
    print(end - start)
    
    start = time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = [val for val in executor.map(primo, number)]
        results = [val for val in executor.map(fatorial, number)]
        results = [val for val in executor.map(tri, number)]
        end = time()
    print('teste paralelo')
    print(end - start)

if __name__ == '__main__':
    main()

