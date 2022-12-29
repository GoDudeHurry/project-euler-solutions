# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
from math import *

class NthPrimeNumber:
    def __init__(self, range):
        self.range = range
        self.listOfPrimes = [2]
        
    def isPrime(self, factor):
        divisor = 2
        while divisor <= int(sqrt(factor)):
            if factor % divisor == 0:
                return False
            divisor += 1
        return True
    
    def getNthPrimeNumber(self):
        count = 1
        num = 3
        while count < self.range:
            if self.isPrime(num):
                count += 1  
                self.listOfPrimes.append(num)
            num +=1          
        return self.listOfPrimes[-1]
    
compute = NthPrimeNumber(10001)
print("The prime number at position %d is %d" % (compute.range, compute.getNthPrimeNumber()))
print(compute.listOfPrimes)