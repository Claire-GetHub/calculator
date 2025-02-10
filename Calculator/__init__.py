import operator as op
from enum import Enum

class Calculator: 
    cal = Enum('cal', [('HEAVY', True), ('SOFT', False)])

    def __init__(self, initalValue: int = None, mode: Enum = cal.SOFT): 
        self.initailValue = initalValue
        self.mode = mode
        self.cache = {}

    def __eq__(self, calc2) -> str:
        return self.initailValue == calc2.initailValue

    def setInitailNumber(self, newNumber: int) -> None:
        self.initailValue = newNumber

    def determineKey(self, operation: op, num1: int, num2: int) -> str:
        """
        Creates a dictionary key for the math cache
        :param num1: The first number in the probkem
        :param num2: The second number in the problem
        :paran operator: The operator to use in the math probkem

        Documenation:
        https://docs.python.org/3/library/operator.html
        """

        if operation == op.add or operation == op.mul:
            numbers = (num1,num2)
            return f"{operation}{min(numbers)} {max(numbers)}"
        else:
            return f"{operation}{num1} {num2}"
        
        




    def performOperation(self,  operation: op, num1: int, num2: int = None) -> int:
        """
        This utilizes the numbers provided and the operation as a function
        to perform math :) If the number2 is not provided then initial value should be used

        :param num1: The first number in the probkem
        :param num2: The second number in the problem
        :paran operator: The operator to use in the math probkem
        """
        num2 = num2 or self.initailValue

        if self.mode == self.cal.HEAVY and (key := self.determineKey(operation, num1, num2)) in self.cache:
            return self.cache[key], "cache"
        else:
            anw = operation(num1, num2)
            if self.mode == self.cal.HEAVY:
                self.cache[key] = anw
            return anw


    def subtract(self, num1, num2: int = None) -> int:
        """
        """
        operation = op.sub
        return self.performOperation(operation, num1, num2)

    def add(self, num1: int, num2: int = None) -> int:
        operation = op.add
        return self.performOperation(operation, num1, num2)
    
    def power(self, num1: int, num2: int = None) -> int:
        operation = op.pow
        return self.performOperation(operation, num1, num2)
        
        








    # def addition(self, num1: int, num2: int = None) -> int:
    #     num2 = num2 if num2 else self.initailValue
    #     numbers = (num1, num2)
    #     if (equation := f"{min(numbers)} + {max(numbers)}") in self.cache:
    #         return self.cache[equation], "cache"
    #     else:
    #         anw = num1 + num2
    #         self.cache[equation] = anw
    #         return anw