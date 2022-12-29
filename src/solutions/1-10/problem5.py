# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

class CommonDividend:
    def __init__(self, range):
        self.range = range
        
    def getGCD(self, a, b):
        while a != b:
            if a > b:
                a = a-b
            elif a < b:
                b = b-a
        return a
    
    def getLCM(self, a, b):
        return int((a*b)/self.getGCD(a, b))
    
    def getSmallestCommonDividend(self):
        lcm, b = 1, 2
        while b <= self.range:
            lcm = self.getLCM(lcm, b)
            b += 1
        return lcm
    
compute = CommonDividend(20)
print(compute.getSmallestCommonDividend())