#Find the product of thirteen adjacent digits in the given 1000 digit number
#that has the greatest product
from math import *

class ProductOfAdjacentDigits:
    def __init__(self, lengthOfProduct, numberAsAString):
        self.digits = len(numberAsAString)
        self.lengthOfProduct = lengthOfProduct
        self.numberAsAString = numberAsAString
        self.numberAsAnArray = []
        for digit in self.numberAsAString:
            self.numberAsAnArray.append(int(digit))
        self.listOfProducts = []
        
    def getSubArray(self, startIndex):
        return self.numberAsAnArray[startIndex : startIndex + self.lengthOfProduct]
    
    def getMaximumProduct(self):
        for startIndex in range(0, self.digits):
            subArray = self.getSubArray(startIndex)
            if 0 not in subArray:
                self.listOfProducts.append(prod(subArray))
            
        return max(self.listOfProducts)
    
compute = ProductOfAdjacentDigits(13, "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450")
print(compute.getMaximumProduct())