class Fraction:
    '''
    This class is designed to allow users to perform basic +,-,/,* operations on 
    fractions as well as see the lowest form of the fraction through its str() method
    '''
    #constructor method
    def __init__(self,top,bottom):
        """constructor
        Arguments:
            top {integer} -- numerator in a fraction
            bottom {integer} -- denominator in a fraction
        Raises: TypeError if parameters are not integers
        """
        #if type(top) != int or type(bottom) != int:
        if not isinstance(top,int) or not isinstance(bottom,int):
            raise TypeError('Incorrect type passed in')
        if top < 0 and bottom < 0:
            top = abs(top)
            bottom = abs(bottom)
        elif bottom < 0:
            top = -top
            bottom = abs(bottom)
        gdc = self.gcd(top,bottom)
        self.__num = top // gdc
        self.__den = bottom // gdc

    #access to num property
    @property
    def num(self):
        return self.__num

    #access to den property
    @property
    def den(self):
        return self.__den

    def __str__(self):
        """String representation of Fraction class
        Returns: {String}
        """
        return '{}/{}'.format(self.__num,self.__den)

    def __add__(self,f2):
        """method to override the standard add method in Python
        Arguments:
            f2 {Fraction} -- Fraction Class Object
        Returns: {Fraction} -- Returns most reduced form of fractions after being added
        """
        new_numerator = self.__num * f2.den + self.__den * f2.num
        new_denominator = self.__den * f2.den
        return Fraction(new_numerator,new_denominator)

    def __sub__(self,f2):
        """method to override the standard substract method in Python
        Arguments:
            f2 {Fraction} -- Fraction Class Object
        Returns: {Fraction} -- Returns most reduced form of fractions after being subtracted
        """
        new_numerator = self.__num * f2.den - self.__den * f2.num
        new_denominator = self.__den * f2.den
        return Fraction(new_numerator,new_denominator)
    
    def __mul__(self,f2):
        """method to override the standard multiply method in Python
        Arguments:
            f2 {Fraction} -- Fraction Class Object
        Returns: {Fraction} -- Returns most reduced form of fractions after being multiplied
        """
        new_numerator = self.__num * f2.num
        new_denominator = self.__den * f2.den
        return Fraction(new_numerator,new_denominator)

    def __truediv__(self,f2):
        """method to override the standard division method in Python
        Arguments:
            f2 {Fraction} -- Fraction Class Object
        Returns: {Fraction} -- Returns most reduced form of fractions after being divided
        """
        new_numerator = self.__num * f2.den
        new_denominator = self.__den * f2.num
        return Fraction(new_numerator,new_denominator)

    def gcd(self,num,den):
        """Finds greatest common demominator in a fraction
        Arguments:
            num {integer}
            den {integer}
        """
        while num%den != 0:
            oldnum = num
            oldden= den
            num = oldden
            den = oldnum%oldden
        return den

    def __eq__(self,f2):
        """Method to show if the fractions of 2 fraction objects are equal"""
        return self.__num * f2.den == self.__den * f2.num

    def __gt__(self,f2):
        """Overrides greater than method"""
        return self.__num * f2.den > self.__den * f2.num

    def __ge__(self,f2):
        """Overrides greater than or equal method"""
        return self > f2 or self == f2
    
    def __lt__(self,f2):
        """Overrides greater than or equal method"""
        return not self > f2

    def __le__(self,f2):
        """Overrides greater than or equal method"""
        return not self > f2 or self == f2
    
    def __ne__(self,f2):
        """Overrides greater than or equal method"""
        return not f2 == self
        #return self.__num * f2.den != self.__den * f2.num
    def __radd__(self,num):
        """Overrides __radd_ method"""
        if num == 0:
            return self
        #elif type(num) == int and num > 0:
        elif isinstance(num,int) and num > 0:
            num = Fraction(num,1)
            return self.__add__(num)
        elif not isinstance(num,int): 
            raise TypeError('Incorrect type passed in')
    def __iadd__(self,num):
        """Overrides __iadd_ method"""
        if num == 0:
            return self
        elif type(num) == int and num > 0:
            num = Fraction(num,1)
            return self.__add__(num)
        else:
            raise TypeError('Incorrect type passed in')
    def __repr__(self):
        """Overrides __repr_ method"""
        return '{}State: {}'.format(self.__class__, self.__str__())