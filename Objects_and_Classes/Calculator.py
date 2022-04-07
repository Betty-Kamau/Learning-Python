# A Simple Calcuator with functions and classes

class Calculator:
    #A constructor with 2 varialbles is declared
    def __init__(self, object1=None, object2=None):
        self.obj1 = int(input("Enter a number: "))
        self.obj2 = int(input("Enter a second number: "))

    #This method performs addition
    def addition(self):
        add = self.obj1 + self.obj2
        print("The sum of the 2 numbers is ", add)

    #This method performs subtraction
    def subtraction(self):
        difference = self.obj1 - self.obj2
        print("The difference of the numbers is ",difference)

    #This method performs multiplication
    def multiply(self):
        total = self.obj1 * self.obj2
        print("The multiplicant of the 2 numbers is ", total)

    #This method performs division
    def divide(self):
        dividend = self.obj1 / self.obj2
        print("The dividend of the numbers is ", dividend)

calc = Calculator()
   
input = int(input("Select 1, 2, 3 or 4 to determine the operation:\n"
                        "1. Addition\n"
                        "2. Subtraction\n"
                        "3. Multiplication\n"
                        "4. Division\n"))

if input == 1:
    calc.addition()

elif input == 2:
    calc.subtraction()

elif input == 3:
    calc.multiply()

elif input == 4:
    calc.divide()

else:
    print(int(input("Choose either 1, 2, 3 or 4")))