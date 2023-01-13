# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
from math import *
from time import *

class SumOfPrimes:
    def __init__(self, limit):
        self.limit = limit
        self.listOfPrimes = [2, 3]
        
    def isPrime(self, number):
        divisor = 2
        for divisor in self.listOfPrimes:
            if divisor > int(sqrt(number)):
                break
            #Divide by list of primes upto the sqrt to optimize the time
            if number % divisor == 0:
                return False
            
        return True
    
    def getSumOfPrimes(self):
        number, prime = 1, 0
        while 6*number + 1 < self.limit:
            print("checking if [6*"+str(number)+"(\'+\' or \'-\')1] is a prime",end="\r")
            if self.isPrime(6*number-1) and (6*number-1 < self.limit):
                self.listOfPrimes.append(6*number-1)
            if self.isPrime(6*number+1) and (6*number+1 < self.limit):
                self.listOfPrimes.append(6*number+1)
            number += 1
            
        return sum(self.listOfPrimes)

compute = SumOfPrimes(2000000)
start = time()
print("\nSum of prime numbers upto %d is"%(compute.limit),compute.getSumOfPrimes())
end = time()
print("\nTime taken by the algorithm : ",end-start,"s")
# print("\n",compute.listOfPrimes)
        