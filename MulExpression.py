'''
Created on Nov 13, 2012

@author: Laura
'''

class MulExpressions(object):
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
        return self.left.getValue() * self.right.getValue()