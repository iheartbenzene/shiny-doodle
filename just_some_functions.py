import math
import numpy as np
from numpy import linalg as la
import scipy as sc
from scipy import linalg as scla
import sklearn as sk

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
    return (a * (1 - r**N))/(1-r)
''' Returns the sum of the geometric sequence from 1 to N where a is the first term, r is the common ratio, and N is the upper bound of the summation. '''

#Fibonacci numbers
def fibonacci_number(n):
    if n < 2:
        return n
    return fibonacci_number(n-1) + fibonacci_number(n-2)
''' Returns a Fibonacci number '''

#Fibonacci sequence
def fibonacci_sequence(n):
    i = 0
    while i < n:
        print(fibonacci_number(i), end=" ")
        i+=1
    return""
''' The Finobacci sequence '''

#Gradient Descent
def gradient_descent(x, y, theta, alpha, m, iterations):
    x_transpose = x.transpose()
    for i in range(iterations):
        hypothesis = np.dot(x, theta)
        errors = hypothesis - y
        
        cost = np.sum(errors ** 2) / (2 * m)
        print("At iteration %d the cose is %f" % (i, cost))
        
        gradient = np.dot(xTrans, loss) / m
        
        theta = theta - alpha * gradient
    return theta
''' The method for gradient descent '''
