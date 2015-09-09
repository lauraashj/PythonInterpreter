'''
Created on Nov 13, 2012

@author: Laura
'''
import abc
from ArithmeticExpression import ArithmeticExpressions

class BinaryExpressions(ArithmeticExpressions):
    def __init__(self):
        '''
        Constructor
        '''
    @abc.abstractmethod
    def getExpression(self):
            return
