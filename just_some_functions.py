import math

#Factorials
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
''' The factorial of some number n '''

#Binomial coefficients
def binomial_coefficient(n, m):
    return factorial(n) / (factorial(m) * factorial(n-m))
''' Binomial Coefficients in the vein of n choose k  or combinations'''

#Seive of Eratosthenes
def sieve_of_eratosthenes(n):
    seq_primes=list(range(2, n + 1))
    sieve_set=set(range(2, n + 1))
    for j in range(0, math.floor(math.sqrt(n)) + 1):
        for k in range(j, math.floor(n / seq_primes[j]) + 1):
            sieve_set.discard(seq_primes[k] * seq_primes[j])
    return sorted(sieve_set)
''' The Sieve of Eratosthenes prints all prime numbers below an upper bound N. Using sum(sieve_of_eratosthenes) will return the sum of the all of the prime values below N. '''

#Definition of a leap year
def is_leap(year):
    leap = False
    if year % 4 == 0:
      leap = True
    if year%400 == 0 and year%4 == 0:
        leap = True
    elif year%100 == 0 and year%4 == 0:
        leap = False
    return leap
''' Just the definition of a leap year. '''

#Nth partial sum
def generic_progression(n, k):
    return k * ((n//k)*((n//k)+1)) / 2
''' Returns the Nth partial sum of the multiples of some number, k,  up to an upper bound, N '''

#Geometric sequence
def geometric_sequence(a, r, N):
    return (a * (1 - r**n))/(1-r)
''' Returns the sum of the geometric sequence from 1 to N where a is the first term, r is the common ratio, and N is the upper bound of the summation. '''

