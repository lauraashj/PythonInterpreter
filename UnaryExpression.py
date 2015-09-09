'''
Created on Nov 13, 2012

@author: Laura
'''
from ArithmeticExpression import ArithmeticExpressions

class UnaryExpressions(ArithmeticExpressions):
    '''
    classdocs
    '''


    def __init__(self, op):
        '''
        Constructor
        '''
        self.op = op
        
    def getExpression(self):
        return self.op.getValue()