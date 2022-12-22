# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers
import time as t

class Palindrome:
    def __init__(self, digits):
        self.digits = digits
        self.limit = 0
        self.highestPalindrome = 0
        self.collectionOfPalindromes = {}
        print("You selected",self.digits,"digit numbers")
        while(self.limit*10 < 10**digits):
            self.limit *= 10
            self.limit += 9
        print("Highest " + str(digits) , "digit number is " + str(self.limit))
    
    def isPalindrome(self, number1, number2):
        number = str(number1*number2)
        reverse = number[::-1]
        return number == reverse
    
    def getCollectionOfPalindromes(self, limit):
        for high in range(limit, 10**(self.digits-1), -1):
            for low in range(high, 10**(self.digits-1), -1):
                if(self.isPalindrome(high, low)):
                    self.collectionOfPalindromes[str(high)+"*" + str(low)] = high*low
        return self.collectionOfPalindromes
        
    def greatestPalindrome(self, limit):
        if len(self.getCollectionOfPalindromes(limit)) > 0 and limit >0:
            self.highestPalindrome = max(self.collectionOfPalindromes.values())
            return
        else:
            print("No Palindromes found!")
                
                
        
compute = Palindrome(2)
start = t.time()
compute.greatestPalindrome(compute.limit)
print("Highest palindrome by multiplying 2 -",compute.digits,"digit numbers  is ",compute.highestPalindrome)
# print(compute.collectionOfPalindromes)
end = t.time()
print("Time taken : %4.16f s"%(end-start))
