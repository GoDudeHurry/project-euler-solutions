# The sum of the squares of the first ten natural numbers is, 385
# The square of the sum of the first ten natural numbers is, 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

class Solution:
    def __init__(self, limit):
        self.limit = limit
        self.sumOfSquares = 0
        self.sumOfNumbers = 0
        self.squareOfSums = 0
        
    def computeSumOfSquares(self):
        for number in range(1, self.limit + 1):
            self.sumOfSquares += number*number
    
    def computeSquareOfSums(self):
        for number in range(1, self.limit + 1):
            self.sumOfNumbers += number
        self.squareOfSums = self.sumOfNumbers * self.sumOfNumbers
    
compute = Solution(100)
compute.computeSquareOfSums()
compute.computeSumOfSquares()
print("Difference is :\t", compute.squareOfSums - compute.sumOfSquares)
