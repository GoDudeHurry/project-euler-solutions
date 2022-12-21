#Find the sum of all the multiples of 3 or 5 below 1000.

class Solution1:
    def __init__(self, number):
        self.number = number
        self.listOfMultiples = []
        self.sumOfMultiples = 0
        
    def getListOfMultiples(self):
        for i in range(1, self.number):
            if i%3 == 0 or i%5 == 0:
                self.listOfMultiples.append(i)
                self.sumOfMultiples += i
        return self.listOfMultiples
    
    def getSumOfMultiples(self):
        return self.sumOfMultiples
    
    
compute = Solution1(1000) 
compute.getListOfMultiples()
print("Sum of multiples : " + str(compute.getSumOfMultiples()))          
            