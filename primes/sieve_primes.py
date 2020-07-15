#!/usr/bin/env python3

from sys import argv
from math import sqrt

def sieve_primes(n):
    """sieve_primes computes the first n primes using the sieve of Eratosthenes
    
    Takes in an integer n and returns an array primes.
    TODO Takes complex numbers and sieves for Gaussian integers
    TODO Take advantage of multithreading using Scala.

    Refer to https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode for more information.
    """
    if int(n) == n:
        n = int(n)
        if n > 1:
            max = int(sqrt(n)) #the largest possible divisor will not be greater than sqrt(n)
            primes = list(range(2,max+1))
            A = [True] * (n-1) #make list of Trues with length off by 1 because 1 is not prime
            for i in range(2,max+1): #for each of possible prime values (2 to sqrt(n))
                if A[i] is True:
                    for j in range(i**2,n-1,i):
                        print(j)
                        A[j] = False
                print(A)
                print(primes)
            # i = list(range(2,max+1))
            return A
        else:
            raise ValueError
    else:
        raise TypeError

if __name__ == '__main__':
    sieve_primes(float(argv[1]))
