#Purpose/ Code Overview:
    #Creates a class called ClassifyingNumbers that has attributes that find
    #the proper factors of a number, informs the user if the number is perfect,
    #abundant, or deficient, finds all perfect numbers below the number, and
    #prints all proper factors of the number.
    
#Inputs/ Outputs: There are no input or output files

#defining class object ClassifyingNumbers
class ClassifyingNumbers:
    """initializing the attributes to describe CassifyingNumbers"""
    def __init__(self, number, propers=[]):
        #number is an integer
        self.number = number
        
        #propers is a list
        self.propers = propers
        
    def properfactors(self):
        """adds all proper factors of a number to the list propers"""
        
        #for loop ranging from 1 to 1+ the number given 
        for n in range(1, self.number+1):
            
            #if the number is divisible by the index (n) then
            if (self.number % n == 0):
                
                #adds the index n to the list propers using append function
                self.propers.append(n)
        
        #removes the number from the list of propers using remove function
        #does this because a number is not a proper factor of itself
        self.propers.remove(self.number)

    def description(self):
        """Informs the user if the number is a perfect, deficient, or abundant 
        number"""
        #sets propers to a blank list
        self.propers = []
        
        #calls the function properfactors to get a list of proper factors for 
        #the number
        self.properfactors()

        #sets the value of the variable x to the sum of numbers in the list
        #propers
        self.x = sum(self.propers)
        
        #if the value of the sum of the propers is equal to the number the 
        #factors are being found
        if self.x == self.number:
            
            #prints statement using fstring that lets the user know that the 
            #number is a perfect number
            print(f"{self.number} is a perfect number!")
            
        #elif means else if
        #if the sum of the proper factors is less than the number
        elif self.x < self.number:
            
            #prints the statement to inform the user that it is a deficient 
            #number
            print(f"{self.number} is a deficient number!")
            
        #if the sum is greater than the number then
        elif self.x > self.number:
            
            #print the statement that lets the user know it is an abundant 
            #number
            print(f"{self.number} is an abundant number!")
        
    def findingperfectnumbers(self):
        """prints a list of the perfect numbers less than the
        specified number"""
        
        #creates list called perfect_numbers
        self.perfect_numbers = []
        
        #loops from 6 to the number specified
        #starts at 6 because that is the first perfect number
        for n in range(6, self.number):
            
            #initialize empty list j
            j = []
            
            #loop from 1 to the index n of the outer loop
            for k in range(1, n):
                
                #if n is divisible by k (with no remainder)
                if (n % k == 0):
                    
                    #add k to the list j
                    j.append(k)
            
            #if the sum of the numbers in the list j is equal to the value n
            if sum(j) == n:
                
                #adds the number n to the perfect_numbers list
                self.perfect_numbers.append(n)
        
        #prints a list of the perfect numbers less than the specified number
        #using an fstring and the print function
        print(f"The perfect numbers less than {self.number} are {self.perfect_numbers}")
        
    def printingpropers(self):
        """Prints and sorts a list of proper factors of a number"""
        
        #calls function properfactors 
        self.properfactors()
        
        #uses list of propers from the function called immediately above and
        #creates a set object and assigns it the name prop which enables 
        #sorting later
        prop = list(set(self.propers))
        
        #sorts the numbers in the prop list by increasing value
        prop.sort()
        
        #prints the list of proper factors of a number
        print(f"The proper factors of {self.number} are {prop}")
        

#testing the code above
Classify = ClassifyingNumbers(500)
Classify.description()        
Classify.findingperfectnumbers()
Classify.printingpropers()

Classify = ClassifyingNumbers(600)
Classify.description()        
Classify.findingperfectnumbers()
Classify.printingpropers()
Classify = ClassifyingNumbers(700)
Classify.description()        
Classify.findingperfectnumbers()
Classify.printingpropers()
