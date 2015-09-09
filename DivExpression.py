'''
Created on Nov 17, 2012

@author: Laura
'''
from BinaryExpression import BinaryExpressions

class DivExpressions(BinaryExpressions):
    '''
    classdocs
    '''
    def __init__(self, left, right):
        '''
        Constructor
        '''
        
        self.left = left
        self.right = right
        
        
    def getExpression(self):
        return self.left.getValue() / self.right.getValue()