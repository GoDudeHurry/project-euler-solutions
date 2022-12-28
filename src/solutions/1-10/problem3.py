# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143

from math import *

class PrimeFactor:
    def __init__(self, number):
        self.number = number
        self.listOfPrimeFactors = []
        
    def isPrime(self, factor):
        divisor = 2
        while divisor <= int(sqrt(factor)):
            if factor % divisor == 0:
                return False
            divisor += 1
        return True
    
    def getPrimeFactors(self):
        if self.number%2 == 0:
                self.listOfPrimeFactors.append(2)
                
        if self.isPrime(self.number):
                self.listOfPrimeFactors.append(self.number)
                return
        else:
            for factor in range(3, ceil(sqrt(self.number)) + 3, 2):
                if self.number%factor == 0 and self.isPrime(factor):
                    self.listOfPrimeFactors.append(factor)
                
                
compute = PrimeFactor(12315464385435)
compute.getPrimeFactors()
print("The prime factors of %d are "%(compute.number),compute.listOfPrimeFactors)
print("The highest prime factor of %d is "%(compute.number),compute.listOfPrimeFactors[-1])