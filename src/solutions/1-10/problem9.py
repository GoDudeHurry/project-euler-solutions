# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

class PythagoreanTriplet:
    def __init__(self):
        self.sum = 1000
        self.triplet = ()
    
    def isTriplet(self, a, b, c):
        return (a**2 + b**2) == c**2
    
    def getTriplet(self):
        for a in range(1, self.sum+1):
            for b in range(a, self.sum-a):
                c = self.sum-a-b
                print("computing : ", (a, b, c),end="\r")
                if self.isTriplet(a, b, c):
                    self.triplet = (a, b, c)
                    return self.triplet
                    
compute = PythagoreanTriplet()
print("\n",compute.getTriplet())
print("Product of the triplet is:", compute.triplet[0]*compute.triplet[1]*compute.triplet[2])